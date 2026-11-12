+++
title = "Gemini 4 Carbonで楽しむ NetHack リメイク"
date = "2026-11-12"
cover = "images/nethack-remake-with-gemini-4-carbon.png"
tags = ["Game", "Gemini", "Blender", "MCP"]
description = "Gemini 4 Carbon と Blender MCP を使って、名作ローグライク NetHack を 3D アクション RPG にリメイクする方法を、実践的なコツやプロセスの解説とともにご紹介します。"
showFullContent = false
readingTime = false
hideComments = false
emoji = "🎮"
+++

こんにちは！今回は Gemini 4 Carbon をテストしながら体験した内容をご紹介したいと思います。何をしたかというと…？ 1987年にリリースされた名作レトロローグライクゲーム「[NetHack](https://www.nethack.org/)」を、現代的な3DアクションRPGとして新しくリメイクしてみました。テキストとASCIIグラフィックだけで繰り広げられるオリジナル版ダンジョン探索の奥深い面白さは、ディアブロをはじめとする後世の数多くのゲームに大きな影響を与え、オープンソースとして公開されているおかげで現在も着実に進化を続けています。

**✨ リメイクデモのプロモーション動画**

{{< youtube id="4KfezQB4aW0" >}}

**実際のプレイ画面**

![NetHack 3D ARPG Remake](images/nethack-agy-3d-arpg.gif)

テキストベースのレトロゲームが、どのようなプロセスを経て現代的な3DアクションRPGへと変貌を遂げたのか気になりませんか？以下にまとめたガイドにゆっくり沿って進めていけば、皆さんも自分だけのレトロゲームリメイクプロジェクトを手軽に始めることができますよ！

# 🛠️ 事前準備

- **Antigravity のインストールとモデルアクセス権の確保:** プロジェクト開発プラットフォームである Antigravity をインストールし、優れたコーディング能力を誇る Gemini 4 Carbon モデルのアクセス権を用意します。
- **3Dアセット自動化環境の構築:** 3Dモデリング用ソフトの Blender をインストールし、MCP (Model Context Protocol) アドオンを追加した後、Antigravity に Blender MCP サーバーを接続します。

> **📌 ちょっとした注意点！**\
公開されているコードリポジトリには、それぞれ独自のライセンス条項があります。個人の学習目的で自由に試すのは問題ありませんが、商用利用したり最終的な成果物を一般公開したりする前には、必ずプロジェクトのライセンスを確認してください！

それでは、上で触れた準備事項を順番にひとつずつ見ていきましょう。

# 💻 Antigravity のインストールとモデルアクセス権

Antigravity のインストール - https://antigravity.google\
Gemini 4 Carbon は [Google AI Ultra プラン](https://one.google.com/about/google-ai-plans/)にご加入いただくとすぐにご利用いただけます。

すべての準備が整ったら Antigravity で新規プロジェクトを作成し、以下のように Gemini 4 Carbon を使用できる状態に設定します。

![Antigravity Setup](images/nethack-agy-1.png)

それでは次のステップに進んでみましょう！

# 🎨 3Dアセット自動化環境の構築

なぜ別の MCP サーバーが必要なのでしょうか？実はこの設定がなくても Carbon を活用して 3D ゲームを開発する分にはまったく問題ありません。しかし MCP を接続すると、3D アセット生成に特化した機能を活用できるようになり、より完成度の高い成果物を得ることができます。すでに使用している他のサーバーがあればそれを活用しても良いですし、初めて触れる方は以下の案内を参考に Blender MCP サーバーを接続してみてください。

Blender のインストール - https://www.blender.org\
Blender MCP Server のインストール - https://projects.blender.org/lab/blender_mcp/wiki/Setup\
Blender MCP Server Add-on のインストール - https://www.blender.org/lab/mcp-server/#add-on

最後に Antigravity に Blender MCP サーバーを追加するには、設定ファイルを直接編集する必要があります。

Customizations > Installed > MCP Servers 項目の横にある「Copy Config File Path」をクリックしてパスをコピーし、お好みのテキストエディタでそのファイルを開きます。

![Antigravity MCP Servers](images/nethack-agy-2.png)
![Antigravity MCP Config](images/nethack-agy-3.png)

私の場合、Windows 環境に cloudrun MCP がすでにインストールされているため皆さんの画面と少し異なる場合がありますが、[公式 Wiki の説明](https://projects.blender.org/lab/blender_mcp/wiki/Setup#mcp-config-file)を参考に、ご自身の環境に合わせて設定を追加してください。

その後、Antigravity を再起動して変更された設定ファイルを読み込むと、以下のように blender 項目の横に緑色のライトが点灯します。これで開発のためのすべての準備が完了しました。

![Antigravity Blender MCP Connected](images/nethack-agy-4.png)

# 🚀 メイン作業の開始

すべての準備が終わったら、エージェントに渡すワンショットプロンプトを作成します。実際に作成に使用したプロンプトは以下の通りです。

```text
/swarm Clone https://github.com/NetHack/NetHack and port it into modern web technology and wasm. Remake it into a 3D Action RPG. Use Blender MCP to generate high quality 3d assets.
```

![Antigravity Prompt](images/nethack-agy-prompt.png)

Swarm 機能を使用すると、サブエージェント (Subagent) が生成され、作業を並列処理します。単一エージェントが自分でレビューする方式の代わりに、コンテキストが分離された独立したエージェントが他のエージェントの成果物を客観的に分析するため、より高品質な作業成果を得ることができます。

右下の権限設定はデフォルト (Default) のままにして主要な作業時にユーザーの承認を求めるようにすることもできますし、「Turbo」モードに設定すると最終成果物が出るまでエージェントが自分で判断して作業を進めます。

コードの規模によって所要時間は異なります。待ち時間の間、エージェントの思考プロセスを観察したり、Swarm UI を通じてタスクがどのように分担されているかをリアルタイムで確認してみるのもおすすめです。

![Antigravity Swarm](images/nethack-agy-swarm.png)

すべての作業が完了すると Antigravity から通知が表示されます。成果物に惜しい部分があれば追加の修正リクエストを送ることができますし、新しいアイデアが浮かんだときに機能追加をリクエストしても自然に対応してくれます。

# 🎁 ボーナス: レトロな雰囲気を加える

ゲームの実装が安定して完了したら、レトロな味付けをして80年代の雰囲気が漂うVHSコンセプトのプロモーション動画まで作ってみましょう！

```text
Create a promotion video with 80s vibe with VHS tape artifacts. Use Lyria 3.5 to generate background music. Use Gemini 3.8 Flash TTS to generate promotional messages.
```

ただし、エージェントがローカル環境で該当モデルにアクセスできるようにするには、事前に [GEMINI_API_KEY を設定](https://aistudio.google.com/docs/api-key)するか、Antigravity の Marketplace から Gemini API プラグインをインストールする必要がある点にご留意ください。

![Antigravity Plugin](images/nethack-agy-plugin.png)

これで最初にご覧いただいたプロモーション動画の制作過程まで、すべて見てきました。

皆さんはどんな素晴らしい作品を作れましたか？

