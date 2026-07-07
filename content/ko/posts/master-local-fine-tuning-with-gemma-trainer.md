+++
title = "`gemma-trainer`로 로컬 파인튜닝 마스터하기"
date = "2026-07-02"
cover = "images/master-local-fine-tuning-with-gemma-trainer.png"
tags = ["Gemma", "Fine-Tuning", "AI", "Local-AI"]
description = "로컬 파인튜닝을 효율적으로 만들어줄 새로운 스킬로 나만의 AI 모델을 직접 제어해 보세요."
showFullContent = false
readingTime = false
hideComments = false
+++

지난 5월에 [`gemma-skills`](https://github.com/google-gemma/gemma-skills) 저장소(repository)를 소개해 드렸던 것 기억하시나요? 많은 분들이 [지난 포스트]({{< relref "posts/a-warm-welcome-to-gemma-skills.md" >}})를 보고 워크플로우를 효율적으로 개선하셨다는 이야기를 들을 때마다 정말 뿌듯하더라고요. (그리고 뭐, 아직 GitHub 스타가 엄청나게 쏟아지는 건 아니지만, 아주 기분 좋은 출발이라고 생각해요! 😉)

하지만 저 역시 커스텀 애플리케이션을 더 많이 만들다 보니 계속 같은 걸림돌에 부딪히게 되었어요. 바로 **'이렇게 훌륭한 기본 모델을 가져와서 어떻게 내 입맛에 맞게 바꿀 것인가'** 하는 문제였죠.

보통 모델을 파인튜닝(미세조정)하려면 복잡한 설정과 헷갈리는 가이드북을 헤집고 다녀야 하잖아요. 이 과정을 군더더기 없이 깔끔하고 빠르게 만들어 드리기 위해, 새로운 스킬인 **`gemma-trainer`** 를 만들었습니다.

# `gemma-trainer`가 무엇인가요?

`gemma-trainer`는 개인 컴퓨터에서 Gemma 모델을 학습시키고 최적화할 수 있도록 도와주는 설계도랍니다. "어떻게 구현해야 하지?" 같은 기술적인 고민은 이 스킬이 알아서 해결해 주니, 여러분은 모델에게 새로운 분야를 가르치거나 원하는 방향으로 행동을 교정하는 등 '프로젝트의 목표'에만 온전히 집중하실 수 있어요.

# 사용하면 좋은 이유

* **더 빠르고 가벼운 학습**: 단일 GPU 학습에는 **[Unsloth](http://unsloth.ai/)** 사용을 권장해요. 속도가 빠를 뿐만 아니라 메모리도 적게 먹어서 개인 PC에서도 부드럽게 잘 돌아간답니다.

* **세 가지 핵심 학습방법**: 새로운 정보를 가르치는 지도 학습 기반 파인튜닝(SFT), 원하는 답변 스타일에 맞추는 직접 선호도 최적화(DPO), 그리고 답변의 점수를 매기는 보상 모델링(RM)까지 차근차근 안내해 드려요.

* **보고 들을 수 있는 모델 만들기**: 텍스트는 물론이고, 이미지와 오디오까지 함께 학습(멀티모달 러닝)시킬 수 있는 명확한 가이드를 포함하고 있어요.

* **어디서나 실행 가능**: 학습시킨 모델을 GGUF 같은 가벼운 포맷으로 빠르게 변환해서, **[LiteRT-LM](https://developers.google.com/edge/litert-lm/models/gemma-4)** 을 통해 스마트폰이나 IoT 기기에서도 가볍게 구동할 수 있어요.

* **늘 최신 상태를 유지하는 모범 사례집**: 이 스킬은 가장 최적화된 설정과 최신 학습 기법으로 계속 업데이트되므로, 여러분은 항상 가장 좋은 방법으로 모델을 학습시킬 수 있어요.

# 실제 활용 사례

이 스킬이 실제로 어떻게 작동하는지 살펴볼까요? [지난 포스트]({{< relref "posts/turning-gemma-4-into-an-old-korean-translator.md" >}})에서 Gemma 4를 한국 고전 문학 전문 번역가로 변신시켰던 기억을 떠올려 보세요. `gemma-trainer`와 함께라면 번거롭게 파이프라인을 직접 조립할 필요가 없어요. 그저 인공지능 에이전트에게 이렇게 한 줄만 말하면 됩니다.

> **"bebechien/HongGildongJeon 데이터셋으로 Gemma 4 E2B를 파인튜닝해줘."**

그러면 `gemma-trainer` 스킬을 장착한 에이전트가 든든한 파트너가 되어 다음과 같은 과정을 함께해 줄 거예요.

1. **데이터 검증**: 데이터 검증 스크립트를 실행해 학습 데이터가 템플릿 요구사항에 잘 맞는지 확인합니다.

2. **파라미터 설정**: 비디오 메모리(VRAM)가 부족해 뻗는 일이 없도록, 모델에게 언어적 뉘앙스를 가르치기에 가장 적절한 LoRA 설정을 골라줍니다.

3. **학습 실행**: 자원을 효율적으로 쓰도록 최적화된 기본 설정을 사용해 학습 세션을 시작합니다.

4. **평가 및 반복**: 모델의 결과물을 살펴보고, 내가 딱 원하는 결과가 나올 때까지 설정을 조금씩 조정합니다.

아래는 에이전트가 오디오 작업을 위해 Gemma 4 12B 모델의 파인튜닝을 시작하는 모습을 보여주는 예시예요.

![audio-tuning start](images/gemma-trainer-audio-tuning-start.png)

설정이 끝나면 에이전트가 지정된 데이터셋을 사용해 본격적인 학습 프로세스에 돌입합니다.

![audio-tuning training](images/gemma-trainer-audio-tuning-training.png)

혹시 실수하더라도 걱정하지 마세요. 에이전트가 뒤에서 든든하게 받쳐주니까요. 예를 들어 제가 실수로 Gemma 4 31B 모델(텍스트와 이미지 전용 모델이라 오디오 기능이 없어요!)을 학습시켜 달라고 요청했을 때, 에이전트는 오디오 튜닝에는 Gemma 4 E2B나 12B 모델을 대신 사용해 보라고 다정하게 제안해 주었답니다.

![audio-tuning fix](images/gemma-trainer-audio-tuning-fix.png)

학습이 끝나면 에이전트가 결과를 보여주고 다음 단계로 무엇을 해야 할지 짚어줍니다.

![audio-tuning finish](images/gemma-trainer-audio-tuning-finish.png)

내 입맛에 딱 맞춘 커스텀 평가 스크립트를 짜달라고 에이전트에게 부탁할 수도 있어요. 이 예시에서는 텍스트 변환의 유사도를 체크하는 스크립트를 만들어 달라고 해봤습니다.

![audio-tuning eval](images/gemma-trainer-audio-tuning-eval.png)

마지막으로 학습 성능을 한눈에 볼 수 있는 종합 보고서를 받게 되는데요, 이걸 보면 다음번 학습 때 어떤 점을 더 개선할 수 있을지 명확하게 알 수 있어요.

![audio-tuning report](images/gemma-trainer-audio-tuning-report.png)

# 직접 해봐요

`gemma-trainer`는 계속 발전하고 구조화된 살아있는 문서예요. 에이전트의 스킬 디렉토리에 쏙 넣어주기만 하면, 여러분의 AI 어시스턴트가 학습 과정을 어떻게 안내해야 할지 곧바로 파악할 수 있답니다.

지금 바로 [저장소(repository)](https://github.com/google-gemma/gemma-skills)를 확인해 보시고, 여러분의 도구 상자에 이 멋진 스킬을 추가해 보세요. 우리 함께 멋진 무언가를 만들어 봐요!

여기까지 읽어주셔서 감사합니다. 즐거운 모델 학습 되세요!
