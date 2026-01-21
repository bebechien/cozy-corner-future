+++
title = "超軽量AIで、自分好みの記事だけが届くフィードをDIYした話。（皆さんもできます！）"
date = "2026-01-19"
cover = "images/embeddinggemma-tuning-lab.png"
tags = ["EmbeddingGemma", "Gemma", "AI"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
emoji = "🛠️"
+++

# 正直、ノイズが多すぎませんか？

AI関連のニュースを追いかけるのは本当に大変です。「技術っぽくて面白そう」なタイトルを斜め読みするのに膨大な時間を費やしても、結局自分が求めている情報とは全然違ったりしますし…。キーワードフィルターも便利ですが、微妙なニュアンスまでは拾ってくれません。

僕が欲しかったのは、単なる正規表現の文字列ではなく、「雰囲気」でニュースをフィルタリングする方法でした。

そこで最近、**EmbeddingGemma Tuning Lab** というツールで遊んでいます。これは、Googleの `embeddinggemma-300m` モデルをファインチューニングして、自分だけの好みを理解させる新しい Hugging Face Space です。

# バイブス・チェック (The Vibe Check)

このプロジェクトの一番の魅力は、巨大なLLMのプロンプト戦略に頼っていないところです。代わりに **[EmbeddingGemma](https://huggingface.co/collections/google/embeddinggemma)** という、3億（300M）パラメータの軽量モデルを使用しています。これは埋め込み（Embedding）モデルなので、テキストをベクトルに変換してくれます。モデルの仕組みやトレーニング方法について詳しく知りたい方は、[僕のブログ記事](https://developers.googleblog.com/ja/gemma-explained-embeddinggemma-architecture-and-recipe/)をチェックしてみてください。

核心となるアイデアはユニークですが効果的です。このシステムは、`MY_FAVORITE_NEWS`（私のお気に入りのニュース）というハードコードされたアンカーフレーズに対する「意味的類似度（Semantic Similarity）」のスコアに基づいています。

デフォルトの状態では、モデルはそのフレーズが何を意味するのか知りません。しかし、ファインチューニングを行うことで、モデルが認識する世界を少しだけ歪めることができます。あなたが *実際に* 好きな記事はその魔法のフレーズに数学的に近づき、嫌いな記事は遠ざけられるようになるのです。

# 「EmbeddingGemma Tuning Lab」: 3つの実行モード

EmbeddingGemma Tuning Lab は単なるトレーニングスクリプトではありません。実験スタイルに合わせて選べる3つの異なるアプリが含まれています。

1. **トレーナー (Gradio):** ここで魔法がかかります。Gradioアプリを立ち上げると、現在の [Hacker News](https://news.ycombinator.com/) のトップ10ストーリーが表示されるので、気に入ったものにチェックを入れるだけ。「Fine-Tune」をクリックすると、裏側で [MultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) を使ってモデルが更新されます。検索結果がリアルタイムで自分の好みにシフトしていく様子を見るのは結構楽しいですよ。
2. **ターミナルビューワー (CLI):** 真のターミナル愛好家のためのツールです。ライブフィードをスクロールできるインタラクティブなCLIアプリで、モデルのスコアに基づいて記事が色分けされます。「良いバイブス」なら緑、スキップなら赤といった具合です。
3. **ウェブビューワー (Flask):** モデルの仕上がりに満足したら、軽量な Flask アプリを使ってみましょう。ローカルサーバー上でスタンドアロンの「ムードリーダー」としてデプロイすれば、自分だけのパーソナライズされたフィードをバックグラウンドで流しておけます。

# 試してみてください

ニュースの無限スクロールをやめて、ニュースの「バイブスチェック」を始めたいなら、ぜひこのSpaceをチェックするかコードを入手してください。データの取得、トレーニングループ、可視化まで全部やってくれます。

* **Spaceをチェック:** [EmbeddingGemma Tuning Lab](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab)
* **コードを見る:** [リポジトリ](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab/tree/main)には、データセットのエクスポートや、ファインチューニング済みモデルをZIPでダウンロードするために必要なものがすべて揃っています。

それでは、良いチューニングライフを！

