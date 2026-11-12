+++
title = "Gemini 4 Carbon으로 만나는 NetHack 리메이크"
date = "2026-11-12"
cover = "images/nethack-remake-with-gemini-4-carbon.png"
tags = ["Game", "Gemini", "Blender", "MCP"]
description = "Gemini 4 Carbon과 Blender MCP를 활용해 고전 로그라이크 명작 NetHack을 3D 액션 RPG로 리메이크하는 과정과 노하우를 소개합니다."
showFullContent = false
readingTime = false
hideComments = false
+++

안녕하세요! 오늘은 Gemini 4 Carbon을 테스트 하면서 경험했던 내용을 소개하고자 합니다. 무엇을 했냐고요? 1987년에 출시된 명작 레트로 로그라이크 게임 [NetHack](https://www.nethack.org/)을 현대적인 3D 액션 RPG로 새롭게 리메이크 해보았답니다. 텍스트와 ASCII 그래픽만으로 펼쳐지던 오리지널 던전 탐험의 깊은 재미는 디아블로를 비롯한 후대 수많은 게임에 커다란 영감을 주었고, 오픈소스로 공개된 덕분에 지금까지도 꾸준히 발전해 오고 있습니다.

**✨ 리메이크 데모 프로모션 영상**

{{< youtube id="4KfezQB4aW0" >}}

**실제 게임 동작 화면**

![NetHack 3D ARPG Remake](images/nethack-agy-3d-arpg.gif)

텍스트 기반의 고전 게임이 어떠한 과정을 거쳐 현대적인 3D 액션 RPG로 탈바꿈했는지 궁금하지 않으신가요? 아래 정리해 둔 단계별 가이드를 천천히 따라오시면, 여러분도 자신만의 레트로 게임 리메이크 프로젝트를 손쉽게 시작해 보실 수 있습니다!

# 🛠️ 준비사항

- **Antigravity 설치 및 모델 접근 권한 확보:** 프로젝트 개발 플랫폼인 Antigravity를 설치하고, 뛰어난 코딩 능력을 지원하는 Gemini 4 Carbon 모델의 접근 권한을 준비합니다.
- **3D 에셋 자동화 환경 구축:** 3D 모델링용 Blender를 설치하고, MCP(Model Context Protocol) 애드온을 추가한 뒤 Antigravity에 Blender MCP 서버를 연결합니다.

> **📌 잠깐만요!** \
공개 코드 저장소마다 고유한 라이선스 약관이 적용됩니다. 개인 학습 목적으로 자유롭게 실험해 보시는 것은 좋지만, 상업적으로 이용하거나 최종 결과물을 외부에 공개하기 전에는 반드시 해당 프로젝트의 라이선스를 먼저 확인해 주세요!

그럼 위에서 언급한 준비 사항을 순서대로 하나씩 살펴보겠습니다.

# 💻 Antigravity 설치 및 모델 접근권

Antigravity 설치 - https://antigravity.google \
Gemini 4 Carbon은 [Google AI Ultra 플랜](https://one.google.com/about/google-ai-plans/)에 가입하시면 바로 이용하실 수 있습니다.

모든 준비를 마치셨다면 Antigravity에서 새 프로젝트를 생성하고, 아래와 같이 Gemini 4 Carbon을 사용할 수 있는 상태로 설정합니다.

![Antigravity Setup](images/nethack-agy-1.png)

그럼 다음 단계로 진행해 볼까요?

# 🎨 3D 에셋 자동화 환경 구축

왜 별도의 MCP 서버가 필요할까요? 사실 이 설정이 없어도 Carbon을 활용해 3D 게임을 개발하는 데는 전혀 무리가 없습니다. 하지만 MCP를 연결하면 3D 에셋 생성에 특화된 기능들을 활용할 수 있어 훨씬 완성도 높은 결과물을 얻을 수 있습니다. 기존에 사용 중인 다른 서버가 있다면 그것을 활용하셔도 좋으며, 처음 접하신다면 아래 안내를 따라 Blender MCP 서버를 연결해 보세요.

Blender 설치 - https://www.blender.org \
Blender MCP Server 설치 - https://projects.blender.org/lab/blender_mcp/wiki/Setup \
Blender MCP Server Add-on 설치 - https://www.blender.org/lab/mcp-server/#add-on

마지막으로 Antigravity에 Blender MCP 서버를 추가하려면 설정 파일을 직접 수정해야 합니다.

Customizations > Installed > MCP Servers 항목 옆의 “Copy Config File Path”를 클릭해 경로를 복사한 다음, 원하는 텍스트 에디터로 해당 파일을 열어 줍니다.

![Antigravity MCP Servers](images/nethack-agy-2.png)
![Antigravity MCP Config](images/nethack-agy-3.png)

제 경우에는 Windows 환경에 cloudrun MCP가 이미 설치되어 있어 여러분의 화면과 조금 다를 수 있지만, [공식 Wiki 설명](https://projects.blender.org/lab/blender_mcp/wiki/Setup#mcp-config-file)을 참고하여 사용자의 환경에 맞게 설정을 추가해 주시면 됩니다.

이후 Antigravity를 재실행하여 변경된 설정 파일을 불러오면, 아래와 같이 blender 항목 옆에 녹색 불이 들어옵니다. 이제 개발을 위한 모든 준비가 완료되었습니다.

![Antigravity Blender MCP Connected](images/nethack-agy-4.png)

# 🚀 본 작업 시작하기

모든 준비를 끝냈다면 에이전트에 전달할 원샷 프롬프트를 작성합니다. 실제 작성에 사용한 프롬프트는 다음과 같습니다.

```text
/swarm Clone https://github.com/NetHack/NetHack and port it into modern web technology and wasm. Remake it into a 3D Action RPG. Use Blender MCP to generate high quality 3d assets.
```

![Antigravity Prompt](images/nethack-agy-prompt.png)

Swarm 기능을 사용하면 서브 에이전트(Subagent)들이 생성되어 작업을 병렬로 처리합니다. 단일 에이전트가 스스로 검토하는 방식 대신, 컨텍스트가 분리된 독립된 에이전트가 다른 에이전트의 결과물을 객관적으로 분석하기 때문에 한층 더 고품질의 작업물을 얻을 수 있습니다.

우측 하단의 권한 설정은 기본값(Default)으로 두어 주요 작업 시 사용자 승인을 받도록 유도할 수 있으며, “Turbo” 모드로 설정할 경우 에이전트가 최종 결과물이 나올 때까지 스스로 판단하여 작업을 진행합니다.

코드의 규모에 따라 소요 시간은 달라질 수 있습니다. 대기 시간 동안 에이전트의 사고 과정을 관찰하거나, Swarm UI를 통해 업무가 어떻게 분담되고 있는지 실시간으로 확인해 보시는 것도 좋습니다.

![Antigravity Swarm](images/nethack-agy-swarm.png)

모든 작업이 완료되면 Antigravity에서 알림이 표시됩니다. 결과물에서 아쉬운 부분이 있다면 추가 수정 요청을 전달할 수 있으며, 새로운 아이디어가 떠올랐을 때 기능 추가를 요청해도 자연스럽게 처리해 줍니다.

# 🎁 보너스: retro 감성 더하기

게임 구현이 안정적으로 마무리되었다면, 레트로한 감성을 더해 80년대 느낌이 물씬 나는 VHS 컨셉의 프로모션 영상까지 제작해 보세요!

```text
Create a promotion video with 80s vibe with VHS tape artifacts. Use Lyria 3.5 to generate background music. Use Gemini 3.8 Flash TTS to generate promotional messages.
```

단, 에이전트가 로컬 환경에서 해당 모델에 접근할 수 있도록 [GEMINI_API_KEY를 미리 설정](https://aistudio.google.com/docs/api-key)하거나, Antigravity의 Marketplace에서 Gemini API plugin을 설치해야 한다는 점을 유의해 주세요.

![Antigravity Plugin](images/nethack-agy-plugin.png)

이로써 처음에 보셨던 프로모션 동영상 제작 과정까지 모두 살펴보았습니다.

여러분은 어떤 멋진 결과물을 만드셨나요?

