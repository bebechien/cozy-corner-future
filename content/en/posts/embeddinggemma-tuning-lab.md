+++
title = "I Trained a Tiny AI to Judge My Hacker News Feed (And You Can Too)"
date = "2026-01-19"
cover = "images/embeddinggemma-tuning-lab.png"
tags = ["EmbeddingGemma", "Gemma", "AI"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

# It’s just too much noise.

Keeping up with AI News is tough. I spend way too much time skimming past titles that *look* techy but are totally irrelevant to what I’m actually wanting. Keyword filters are brittle because they miss the nuance.

I wanted a way to filter news based on “vibes”, not just regex strings.

So, I’ve been playing around with the **EmbeddingGemma Tuning Lab**, a new Hugging Face Space that provides a tool for fine-tuning Google’s `embeddinggemma-300m` model to understand your specific personal taste.

# The Vibe Check

The coolest part about this project is that it doesn’t rely on a massive LLM prompting strategy. It uses **[EmbeddingGemma](https://huggingface.co/collections/google/embeddinggemma)**, a lightweight 300M parameter model. Because it’s an embedding model, it turns text into vectors. Check out [my blog post](https://developers.googleblog.com/gemma-explained-embeddinggemma-architecture-and-recipe/) if you want to learn more about how the model works and how it was trained.

The core idea is actually pretty funny but effective. The system relies on a "Semantic Similarity" score against a hard-coded anchor phrase: `MY_FAVORITE_NEWS`.

By default, the model doesn't know what that means. But by fine-tuning it, you warp the model's understanding of the universe so that articles you *actually* like are mathematically closer to that magic phrase, and the ones you hate are pushed away.

# The "EmbeddingGemma Tuning Lab": 3 Ways to Run It

The EmbeddingGemma Tuning Lab isn't just a training script; it contains three different apps depending on how you like to experiment:

1. **The Trainer (Gradio):** This is where the magic happens. You load up the Gradio app, it pulls the current top 10 [Hacker News](https://news.ycombinator.com/) stories, and you just check the boxes next to the ones you like. Click "Fine-Tune", and under the hood, it uses [MultipleNegativesRankingLoss](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) to update the model. You can literally watch the semantic search results shift in real-time.

2. **The Terminal Viewer (CLI):** This one is for the true terminal junkies. It’s an interactive CLI app that lets you scroll through the live feed. It color-codes the stories based on the model's score - green for "good vibes," red for skips.

3. **The Web Viewer (Flask):** Once you're happy with the model, there’s a lightweight Flask app included. You can deploy this as a standalone "Mood Reader" on a local server just to have your personalized feed running in the background.

# Try It Out

If you want to stop doomscrolling and start vibe-checking your news, check out the space or grab the code. It handles the data fetching, the training loop, and the visualization for you.

* **Check out the Space:** [EmbeddingGemma Tuning Lab](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab)
* **See the Code:** The [repo](https://huggingface.co/spaces/google/embeddinggemma-tuning-lab/tree/main) includes everything you need to export your dataset and download your fine-tuned model as a ZIP.

Happy tuning!

