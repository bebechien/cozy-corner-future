---
emoji: 🧙‍♂️
published: true
title: '`gemma-trainer`でローカルファインチューニングをマスターしよう'
topics:
- Gemma
- Fine-Tuning
- AI
- Local-AI
type: tech
---
![cover](https://bebechien.github.io/cozy-corner-future/images/master-local-fine-tuning-with-gemma-trainer.png)

去る5月に [`gemma-skills`](https://github.com/google-gemma/gemma-skills) リポジトリを紹介したのを覚えていますか？ [前回の記事](https://zenn.dev/bebechien/articles/a-warm-welcome-to-gemma-skills)を参考にワークフローを効率化できた、という声をたくさんいただき、本当に嬉しく思っています（GitHubのスターがまだ山ほどついているわけではないけれど、最高のスタートを切れたんじゃないかな、なんて思っています！😉）。

ただ、私自身もカスタムアプリケーションをいくつか作っていく中で、いつも同じ壁にぶつかっていました。それは、**「この素晴らしいベースモデルを、どうやって自分の特定のニーズに合わせて最適化するか」** という問題です。

通常、モデルのファインチューニング（微調整）といえば、複雑な設定や分かりにくいガイドとにらめっこする作業がつきものですよね。このプロセスをシンプルかつスピーディーにするために、今回新しいスキル **`gemma-trainer`** を作りました。

# `gemma-trainer` とは？

`gemma-trainer` は、手元のパソコンでGemmaモデルをトレーニング・適応させるための「設計図」です。「どうやるか」という技術的な手順はこれにお任せできるので、皆さんはモデルに新しい専門知識を教えたり、好みの挙動に調整したりといった、プロジェクト本来の目的に集中できます。

# おすすめしたい理由

* **より速く、より軽いトレーニング**: 1枚のGPUでトレーニングを行う場合は **[Unsloth](http://unsloth.ai/)** の使用を推奨しています。高速なだけでなく、メモリ消費も抑えられるので、個人用のPCでもサクサク動かせます。

* **3つの主要なアプローチ**: 新しい知識を教える「教師ありファインチューニング（SFT）」、好みの出力に合わせる「直接好みの最適化（DPO）」、そして回答の質を評価する「報酬モデリング（RM）」まで、丁寧にガイドします。

* **モデルに「目」と「耳」を**: テキストだけでなく、画像や音声も一緒に学習（マルチモーダル学習）させるための分かりやすい手順が含まれています。

* **どこでも動かせる**: トレーニングしたモデルをGGUFなどの軽量フォーマットにサクッと変換し、**[LiteRT-LM](https://developers.google.com/edge/litert-lm/models/gemma-4)** を使ってスマートフォンやスマート家電（IoTデバイス）上で軽快に動かせます。

* **常に最新のベストプラクティス**: このスキルは、最も最適化された設定や最新のトレーニング手法で随時アップデートされるため、いつでもベストな方法を選択できます。

# 具体的なユースケース

実際の動きをイメージするために、[前回の記事](https://zenn.dev/bebechien/articles/turning-gemma-4-into-an-old-korean-translator)でGemma 4を韓国古典文学の専門翻訳家に変身させたときのことを思い出してみましょう。`gemma-trainer` があれば、面倒なパイプラインを自分で組み立てる必要はありません。AIエージェントにこう話しかけるだけでOKです。

> **「dataset bebechien/HongGildongJeon で Gemma 4 E2B をファインチューニングして」**

すると、`gemma-trainer` スキルを身につけたエージェントが、頼れるパートナーとして次のように並走してくれます。

1. **データの検証**: バリデーションスクリプトを走らせ、トレーニングデータがテンプレートの要求仕様を満たしているかチェックします。

2. **パラメータの設定**: ビデオメモリ（VRAM）不足でエラーにならないよう、言語のニュアンスをうまく学習させるための最適なLoRA設定を選んでくれます。

3. **トレーニングの実行**: リソース効率が良く最適化されたデフォルト設定を使って、トレーニングセッションを開始します。

4. **評価と改善（イテレーション）**: モデルのパフォーマンスを確認し、思い通りの結果が出るまで設定を微調整します。

以下は、エージェントが音声タスク用にGemma 4 12Bモデルのファインチューニングを開始したところです。

![audio-tuning start](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-start.png)

設定が終わると、エージェントは指定されたデータセットを使ってトレーニングを開始します。

![audio-tuning training](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-training.png)

もしうっかり間違えてしまっても、エージェントがしっかりフォローしてくれます。例えば、私が間違えてGemma 4 31Bモデル（これはテキストと画像用のモデルなので、音声機能はありません！）のトレーニングを頼んでしまったとき、エージェントは「音声のチューニングなら、代わりにGemma 4 E2Bか12Bを使ってみたらどうですか？」と優しく提案してくれました。

![audio-tuning fix](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-fix.png)

トレーニングが完了すると、エージェントが結果を提示し、次のステップを教えてくれます。

![audio-tuning finish](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-finish.png)

さらに、特定の好みに合わせてカスタム評価スクリプトを書いてもらうよう、エージェントにお願いすることもできます。今回は、文字起こしの類似度をチェックするスクリプトを作ってもらいました。

![audio-tuning eval](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-eval.png)

最後に、トレーニング全体のパフォーマンスをまとめた包括的なレポートが届きます。これを見れば、次のトレーニングでどこを改善すればいいかが一目瞭然です。

![audio-tuning report](https://bebechien.github.io/cozy-corner-future/images/gemma-trainer-audio-tuning-report.png)

# 試してみましょう

`gemma-trainer` は、常に進化を続ける構造化されたドキュメントです。エージェントのスキルディレクトリにぽんと放り込むだけで、AIアシスタントはすぐに手順を理解し、あなたをガイドできるようになります。

ぜひ [リポジトリ](https://github.com/google-gemma/gemma-skills) をチェックして、皆さんのツールボックスにこのスキルを追加してみてください。一緒に面白いものを作りましょう！

最後まで読んでいただきありがとうございました。それでは、楽しいトレーニングを！