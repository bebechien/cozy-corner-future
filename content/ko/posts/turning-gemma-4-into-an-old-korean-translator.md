+++
title = "Gemma 4를 옛한글 번역기로 변신시키기"
date = "2026-06-15"
cover = "images/tuning-gemma-4-into-an-old-korean-translator.png"
tags = ["Fine-tuning", "Gemma", "AI"]
description = "Gemma 4를 파인튜닝하여 고전 한국어를 현대 한국어로 번역하는 모델을 구축한 경험을 소개합니다."
showFullContent = false
readingTime = false
hideComments = false
+++

오래된 책에는 특유의 아름다움이 있어요. 빛바랜 종이 냄새, 책장을 넘길 때의 감촉, 그리고 여러 세대를 버텨온 이야기들까지. 하지만 조선시대 소설인 *[홍길동전](https://ko.wikipedia.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84)* 같은 고전 한국어 문학을 막상 펼쳐보면, 시간의 흐름이 언어에 남긴 흔적을 금방 실감하게 됩니다.

띄어쓰기도 없고, 아래아(ㆍ)나 여린히읗(ㆆ)처럼 지금은 사라진 옛 글자들이 가득해서, 소설을 읽는다기보다는 아름답고 오래된 암호를 푸는 것 같은 기분이 들거든요. 원어민인 우리에게도 그 언어적인 간극은 생각보다 정말 큽니다.

그래서 과거와 현재를 연결하는 디지털 다리를 놓아보고자 [이 튜토리얼](https://colab.research.google.com/github/google-gemma/cookbook/blob/main/tutorials/Translator_of_Old_Korean_Literature.ipynb)을 준비해 봤어요. **[Gemma 4 E2B (IT)](https://huggingface.co/google/gemma-4-E2B-it)** 를 활용해 고전 한국어를 매끄러운 현대 한국어로 바꾸어 주는 소박한 번역기를 만들어 보려고 합니다.

# 학습을 위한 레시피

부담 없이 도전해 볼 수 있도록, Google Colab에서 NVIDIA T4 GPU(16GB) 환경으로 진행했습니다.

## 1. 환경 설정

먼저 우리가 가장 좋아하는 오픈소스 도구들을 불러옵니다. Hugging Face의 `transformers`, 학습 루프를 위한 `trl`, 그리고 거대한 서버 클러스터 없이도 가볍게 모델을 파인튜닝할 수 있게 도와줄 LoRA(Low-Rank Adaptation)용 `peft`를 챙겨줍니다.

## 2. 재료 모으기

데이터로는 퍼블릭 도메인으로 공개된 *[홍길동전](https://ko.wikisource.org/wiki/%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_(36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8))* 원문과, Creative Commons 라이선스로 공개된 `직지프로` 님의 아름다운 [현대어 번역본](https://ko.wikisource.org/wiki/%EB%B2%88%EC%97%AD:%ED%99%8D%EA%B8%B8%EB%8F%99%EC%A0%84_(36%EC%9E%A5_%EC%99%84%ED%8C%90%EB%B3%B8))을 쌍으로 묶어 사용했습니다.

Gemma가 편안하게 학습할 수 있도록 데이터를 대화 형태로 구조화하고, 명확한 `system` 프롬프트로 모델의 방향을 잡아주었어요.

```json
[
  {"role": "system", "content": "Translate Classical Korean into Modern Korean."},
  {"role": "user", "content": "됴션국셰둉ᄃᆡ왕즉위십오연의홍희문밧긔ᄒᆞᆫᄌᆡ상이잇스되"},
  {"role": "assistant", "content": "조선국 세종대왕 즉위 십오년에 홍회문 밖에 한 재상이 있으되,"}
]
```

# 파인튜닝 전의 모습

Gemma에게 따로 학습을 시키기 전에 먼저 가벼운 베이스라인 테스트를 해봤어요. 기본 모델도 영리하긴 하지만, 고전 문법은 워낙 특수한 영역이니까요. 튜닝을 거치지 않은 Gemma는 나름대로 최선을 다했지만, 너무 길고 직역에 치우친 장황한 설명을 내놓았습니다.

* **고전 원문:** ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* **사람의 번역:** 백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* **Gemma의 첫 예측:** *"Like the color, the heart's praise said, 'The foundation cannot be deeply felt...'"* -> "색과 같이, 마음의 찬사가 말하기를, '그 근본은 깊게 느껴질 수 없으니...'" (영어 기반의 엉뚱한 답변)
* **초기 유사도 점수:** **4.85%** 💔

기본 모델은 시간의 미로 속에서 완전히 길을 잃은 상태였어요. 나침반이 꼭 필요한 순간이었죠.

# 정성껏 Gemma 가르치기

모델을 효율적으로 학습시키기 위해 LoRA를 적용한 PEFT(Parameter-Efficient Fine-Tuning) 설정을 구성했습니다.

```python
from peft import LoraConfig

peft_config = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.05,
    r=16,
    bias="none",
    target_modules="all-linear",
    task_type="CAUSAL_LM",
)
```

**맛을 내는 핵심 비법: `collate_fn`**

챗 모델이 특정 도구처럼 작동하도록 파인튜닝할 때, 모델이 프롬프트(질문) 자체를 다시 쓰는 법을 배우느라 에너지를 낭비하게 두고 싶진 않으실 거예요. 그래서 커스텀 데이터 콜레이터(Data Collator)를 사용해 `system`과 `user` 입력을 마스킹(레이블을 `-100`으로 설정)했습니다. 이렇게 하면 Gemma의 손실(Loss) 계산이 오직 올바른 현대어 답변(`assistant`)을 생성하는 데만 **집중**하게 만들 수 있거든요.

하이퍼파라미터를 조절해 5 에포크(Epochs) 동안 학습률 `2e-5`로 부드럽게 주행하도록 설정한 뒤, 바로 학습 버튼을 눌렀습니다.

# 학습 후의 변화

약간의 기다림 끝에 트레이너가 마법을 부리고 나니, 정말 뿌듯한 결과가 기다리고 있었습니다. 글자 단위 유사도 점수가 무려 79.93%까지 껑충 뛰어올랐거든요!

이제 텍스트를 얼마나 잘 처리하는지 한번 보세요.

* **고전 원문:** ᄇᆡᆨ씨듯고ᄂᆡ심의탄복왈그근본을ᄀᆞᆷ초지아니ᄒᆞ니장부로다ᄒᆞ고ᄌᆡ삼위로ᄒᆞ더라
* **사람의 번역:** 백씨 듣고 내심에 탄복 왈, "그 근본을 감추지 아니하니 장부로다!" 하고, 재삼 위로하더라.
* **파인튜닝된 Gemma의 번역:** 백씨듯 고내심에 탄복 왈, "그 근본을 감초지 아니하니 장부로다." 하고 제삼 위로 하더라.
* **새로운 유사도 점수:** **85.71%** ✨

# 글을 마치며

기술은 늘 우리를 앞만 보고 달리게 만들지만, 제가 가장 좋아하는 기술 프로젝트는 오히려 우리가 과거를 더 또렷하게 돌아볼 수 있도록 도와주는 것들이에요. Gemma 4 같은 가벼운 모델을 조금만 시간을 들여 파인튜닝하면, 문화적 유산을 보존하고 노트북 한 대만 있으면 누구나 옛 지혜와 고전 이야기에 쉽게 다가갈 수 있는 도구를 만들 수 있습니다.

혹시 여러분도 너무 멀게만 느껴지는 역사나 과거의 조각을 발견하신다면, 작은 데이터셋과 한 번의 파인튜닝 세션만으로도 그것을 다시 세상의 밝은 빛 아래로 데려올 수 있다는 걸 기억해 주세요.

나만의 도메인에 맞게 파인튜닝을 진행할 때 참고하기 좋은 워크플로우를 정리해 드립니다:

1. 명확한 목표 정의하기
2. 고품질의 데이터셋 및 평가 계획 준비하기
3. 모델이 잘 학습하고 있는지 검증하기
4. 정량적 지표와 사람의 직관으로 평가하기
5. 배포하고 지속적으로 개선하기

👉 [Gemma Cookbook에서 이 튜토리얼 확인하기](https://www.google.com/url?sa=E&source=gmail&q=https://colab.research.google.com/github/google-gemma/cookbook/blob/main/tutorials/Translator_of_Old_Korean_Literature.ipynb)\
👉 [저희를 응원하고 싶으시다면 레포지토리에 스타(Star)를 눌러주세요!](https://github.com/google-gemma/cookbook)
