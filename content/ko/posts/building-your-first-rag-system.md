+++
title = "나의 첫 RAG 시스템 구축하기"
date = "2026-02-12"
cover = "images/building-your-first-rag-system.png"
tags = ["EmbeddingGemma", "Gemma", "AI"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

# 💎 광석 채굴에서 인사이트 발굴로

*[코어 키퍼(Core Keeper)](https://en.wikipedia.org/wiki/Core_Keeper)* 의 지하 생물 세계를 탐험하든, 소규모 비즈니스의 복잡한 스프레드시트를 탐색하든, "정보 과부하"는 우리의 최종 보스입니다.

**RAG(검색 증강 생성, Retrieval-Augmented Generation)** 시스템은 AI에게 특별한 가이드북을 쥐여주는 것과 같습니다. AI가 일반적인 학습 데이터에만 의존하는 대신, 게임 위키나 연구 노트, 법률 계약서 같은 '나만의 특정 데이터'를 참조하여 정확한 답변을 제공하게 되죠.

여기 **[Gemma 3 4B](https://huggingface.co/google/gemma-3-4b-it)** 와 **[EmbeddingGemma](https://huggingface.co/google/embeddinggemma-300m)** 를 사용하여 프라이빗한 로컬 지식 기반(Knowledge Base)을 구축하는 방법을 소개합니다.

# 🛠️ 제작대 (기술 스택)

이를 위해 우리는 "로컬 우선(Local-First)" 접근 방식을 사용할 거예요. 즉, 데이터가 컴퓨터 밖으로 절대 나가지 않는다는 뜻입니다. 비밀 기지의 좌표(또는 중요한 고객 정보)를 안전하게 지키기에 완벽하죠.

* **두뇌 (LLM):** `gemma3:4b` - 구글의 작고 매우 효율적인 모델입니다.
* **사서 (임베더):** `embeddinggemma` - 데이터를 검색할 수 있도록 "색인화"하는 특화된 모델입니다.
* **서버:** **[Ollama](https://ollama.com/)** - 내 PC에서 이 모델들을 구동해 주는 엔진입니다.
* **인터페이스:** **[AnythingLLM](https://anythingllm.com/)** - 채팅창처럼 생겼지만 문서 저장 같은 무거운 작업을 모두 처리해 주는 사용자 친화적인 앱입니다.

참고: 2026년 로컬 AI의 가장 좋은 점 중 하나는 도구들이 "플러그 앤 플레이" 방식이라는 거예요. 기술적 숙련도에 따라 서버와 UI를 자유롭게 섞어 쓸 수 있습니다. 예를 들어, Ollama 대신 [LM Studio](https://lmstudio.ai/)를 사용하거나, AnythingLLM 대신 [Open WebUI](https://openwebui.com/)를 사용할 수도 있어요. 다양한 도구들을 실험해보세요!

# 📖 1단계: 재료 모으기

먼저, "단일 진실 공급원(Source of Truth)"을 정해야 합니다.

* **게이머라면:** 보스 공략법과 제작 레시피를 추적하기 위해 *[코어 키퍼 위키](https://corekeeper.atma.gg/en/Core_Keeper_Wiki)* 를 사용해 보세요.
* **직장인이라면:** PDF 폴더나 프로젝트 로그, 또는 전문 웹사이트가 될 수도 있습니다.

# ⚙️ 2단계: 작업장 차리기 (Ollama)

*(간단한 팁: 이런 4B 모델을 원활하게 실행하려면 약 8GB의 VRAM이 필요합니다!)*

Ollama를 다운로드하고 터미널에서 다음 두 명령어를 실행하여 모델들을 다운로드하세요:

```shell
# Download the language model
ollama pull gemma3:4b

# Download the embedding model
ollama pull embeddinggemma

```

# 🖥️ 3단계: 인터페이스 설정하기 (AnythingLLM)

**AnythingLLM**을 열고 다음 단계에 따라 모델을 연결해 보세요:

1. **LLM 설정:** 공급자를 **Ollama**로 설정하고 `gemma3:4b`를 선택합니다. 이 모델은 검색된 문맥(context)을 읽고 사용자에게 제공할 최종 답변을 구성하는 "화자(speaker)" 역할을 합니다.
2. **임베더 설정:** **Ollama**를 선택하고 `embeddinggemma`를 고르세요. 이 모델은 여러분의 "검색 엔진" 역할을 하는 전용 고성능 임베딩 모델입니다.
3. **업로드:** "워크스페이스(Workspace)"를 만들고 파일(*코어 키퍼* 위키 페이지나 업무 문서 등)을 끌어다 놓습니다. 그리고 **"Save and Embed(저장 및 임베드)"**를 클릭하세요.

# ⚔️ 4단계: 내 지식 기반 활용하기

이제 여러분의 데이터와 직접 채팅할 수 있습니다.

* **게임 질문:** *"흉측한 질량체(Abominouse Mass)를 어떻게 쓰러뜨릴 수 있어?"*
* **업무 질문:** *"3분기 마케팅 계약서의 주요 조항을 요약해 줘."*

Gemma 3 4B는 단순히 "추측"하는 것이 아니라, 파일에서 특정 텍스트를 찾아내어 설명해 줍니다.

나만의 지식 기반을 갖추기 전과 후, AI에게 질문했을 때의 차이를 확인해 보세요:

* Before: 문맥이 없어서 AI가 일반적이거나 모호하거나 틀린 답을 제공하는 모습.

![before](images/building-your-first-rag-system-before.png)

* After: AI가 업로드된 문서를 출처로 인용하여 정확하고 정밀한 답변을 제공하는 모습.

![after](images/building-your-first-rag-system-after.png)

# 👨🏻‍💻 내 데이터에 직접 적용해 보기

이것을 직접 구축함으로써, 여러분은 단순한 AI 사용자가 아니라 '설계자(Architect)'가 되었습니다. 게임 플레이를 최적화하든 비즈니스 워크플로우를 개선하든, 이제 여러분이 아는 것을 정확히 알고 있는 100% 프라이빗 오프라인 비서가 생긴 셈이죠.

지금까지 *코어 키퍼*를 예로 들었지만, 이 "빌드"는 전문적인 현장 업무에서 진정한 구원자가 될 수 있습니다:

* **현장 연구원:** **인터넷이 전혀 안 되는** 외딴 야생 지역에 있다고 상상해 보세요. 출발하기 전에 AI에게 식물 도감, 이전 탐험 일지, 지질도 등 전체 라이브러리를 입력해 둘 수 있습니다.
* **작가:** 내 소중한 지적 재산(IP)을 클라우드에 올리지 않고도, 초안 챕터들을 입력하여 세계관의 일관성을 확인할 수 있습니다.
* **홈 셰프:** 뒤죽박죽인 레시피 스크린샷 폴더를 검색 가능한 나만의 "디지털 요리책"으로 바꿀 수 있습니다.

> **최고의 장점:** **Gemma 3 4B**와 **EmbeddingGemma**를 로컬에서 사용하기 때문에 시스템은 100% **오프라인**으로 작동합니다. 데이터가 절대 컴퓨터 밖을 벗어나지 않으므로, 위성 연결 없이 즉각적인 답변이 필요한 현장 연구원들에게 완벽한 동반자가 되어줍니다.

