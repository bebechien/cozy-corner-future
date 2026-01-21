+++
title = "해커 뉴스 보다가 지쳐서, 저 대신 뉴스 골라주는 'AI 심사위원'을 직접 만들었습니다."
date = "2026-01-19"
cover = "images/embeddinggemma-tuning-lab.png"
tags = ["EmbeddingGemma", "Gemma", "AI"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

# 뉴스가 너무 많아서 현기증 날 지경이에요.

쏟아지는 AI 뉴스를 따라가는 건 정말 힘든 일입니다. 그럴싸해 보이는 기술 관련 제목들을 훑어보느라 시간을 엄청 쓰지만, 정작 제가 진짜 원하는 내용과는 거리가 먼 경우가 너무 많거든요. 키워드 필터링은 너무 딱딱해서 그 미묘한 뉘앙스를 놓치기 일쑤고요.

저는 단순한 정규표현식 문자열이 아니라, 저만의 "느낌"에 맞춰 뉴스를 걸러낼 방법이 필요했습니다.

그래서 요즘 **EmbeddingGemma Tuning Lab**을 가지고 이것저것 시도해보고 있습니다. 이건 구글의 `embeddinggemma-300m` 모델을 미세 조정(fine-tuning)해서 여러분만의 취향을 이해하도록 만드는 새로운 Hugging Face Space 입니다.

# 바이브 체크 (The Vibe Check)

이 프로젝트의 가장 매력적인 점은 거대한 LLM 프롬프트 전략에 의존하지 않는다는 거예요. 대신 **[EmbeddingGemma](https://huggingface.co/collections/google/embeddinggemma)** 라는 가벼운 3억(300M) 파라미터 모델을 사용합니다. 임베딩 모델이기 때문에 텍스트를 벡터로 변환해 주죠. 모델의 작동 원리나 훈련 방식이 더 궁금하시다면 [제 블로그 글](https://developers.googleblog.com/ko/gemma-explained-embeddinggemma-architecture-and-recipe/)을 참고해 보세요.

핵심 아이디어는 꽤 재밌으면서도 효과적입니다. 이 시스템은 `MY_FAVORITE_NEWS`(내가_좋아하는_뉴스)라는 하드코딩된 기준 문구와의 "의미론적 유사성(Semantic Similarity)" 점수를 기반으로 작동하거든요.

기본적으로 모델은 저 문구가 무슨 뜻인지 모릅니다. 하지만 미세 조정을 통해 모델이 바라보는 세상을 살짝 비틀어 주는 거죠. 여러분이 *실제로* 좋아하는 기사는 저 마법의 문구와 수학적으로 가까워지게 하고, 싫어하는 기사는 멀리 밀어내도록 말이에요.

# "EmbeddingGemma Tuning Lab": 3가지 실행 방법

EmbeddingGemma Tuning Lab은 단순한 훈련 스크립트가 아닙니다. 여러분의 실험 스타일에 맞춰 골라 쓸 수 있는 세 가지 앱이 포함되어 있어요.

1. **트레이너 (Gradio):** 마법이 일어나는 곳입니다. Gradio 앱을 실행하면 [Hacker News](https://news.ycombinator.com/)의 현재 인기 기사 10개를 불러옵니다. 그저 마음에 드는 기사 옆에 체크박스를 표시하기만 하면 돼요. "Fine-Tune"을 클릭하면 내부적으로 [MultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss)를 사용해 모델을 업데이트합니다. 검색 결과가 내 취향에 맞춰 실시간으로 변하는 걸 눈으로 직접 확인할 수 있죠.
2. **터미널 뷰어 (CLI):** 진정한 터미널 덕후들을 위한 도구입니다. 라이브 피드를 스크롤 할 수 있는 대화형 CLI 앱인데요, 모델 점수에 따라 기사 색깔이 바뀝니다. "좋은 느낌"은 초록색, 넘길 글은 빨간색으로 표시되죠.
3. **웹 뷰어 (Flask):** 모델이 마음에 들게 훈련되었다면, 가벼운 Flask 앱을 사용해 보세요. 로컬 서버에 독립형 "내 마음을 읽는 피드(Mood Reader)"로 띄워두고 백그라운드에서 나만의 뉴스 피드를 돌려볼 수 있습니다.

# 직접 해보세요

무한 스크롤은 이제 그만하고 뉴스에 "바이브 체크"를 시작하고 싶다면, 이 Space를 확인하거나 코드를 가져가세요. 데이터 가져오기부터 훈련 루프, 시각화까지 다 처리해 줍니다.

* **Space 구경하기:** [EmbeddingGemma Tuning Lab](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab)
* **코드 보기:** [이 저장소](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab/tree/main)에는 데이터셋 내보내기 및 훈련된 모델을 ZIP으로 다운로드하는 데 필요한 모든 것이 들어 있습니다.

즐거운 튜닝 되세요!

