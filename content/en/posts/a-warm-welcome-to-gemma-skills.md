+++
title = "A Warm Welcome to `gemma-skills`"
date = "2026-05-29"
cover = "images/gemma-skills.png"
tags = ["Gemma", "AI", "Agent"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

**Gemma**, a family of open models, are lightweight, remarkably capable, and have a wonderful "tunability" that makes them perfect for personal projects and enterprise-grade applications alike. But as the ecosystem grew, I found myself asking the same questions over and over: 
* *Which exact model size fits my constraint?* 
* *How do I build an application powered by Gemma that does XYZ?* 
* *How to deploy a Gemma model to production on Google Cloud for my team to use?*

To solve this, we put together a living repository called [**`gemma-skills`**](https://github.com/google-gemma/gemma-skills) (which we're releasing!). It's a curated, structured collection of developer *skills* designed to help both humans and agentic AI assistants build beautiful applications with Gemma models without the friction.

Let's take a walk through what’s inside!

# The Heart of the Repo: `gemma-dev`

At the center of the repository is our first major skill: [`gemma-dev`](https://github.com/google-gemma/gemma-skills/tree/main/skills/gemma-dev). It's a skill file (`SKILL.md`) that serves as a blueprint. It's designed for agents to find what are the latest capabilities, model sizes, good practices, and resources to build with Gemma.

# Keeping Pace with Rapid Ecosystem Evolution

The Gemma ecosystem moves fast, with new models, libraries, and best practices emerging constantly. For developers using foundational LLMs like Gemini, keeping assistant workflows perfectly synced with these rapid releases is a common challenge. Because foundational models are trained on vast, fixed datasets, they don't automatically inherit the day-one nuances of a rapidly evolving framework. This can manifest in a few typical development scenarios:

* **Navigating Version Transitions:** General-purpose assistants may default to established standards (like Gemma 2 or 3) even when your project is ready to leverage the latest capabilities of Gemma 4.
* **Aligning with Modern Libraries**: Recommendations might occasionally lean toward older API patterns rather than the latest optimized packages.
* **Integrating Next-Gen Features:** Cutting-edge implementation details (e.g. Multi-Token Prediction (MTP) or specialized formatting) require specialized context to execute flawlessly.

The *gemma-skills* repository bridges this gap. By providing "live" best practices and structured skill documents directly into your development workflow, we ensure your AI assistant has immediate access to the most current, efficient, and reliable implementation patterns available today.

# How to Use This Repo with Antigravity

These skills are designed to be entirely harness-agnostic. They integrates into any developer workflow or agentic tool, from Gemini to Claude. To get started quickly, whether you're leveraging these as clean templates or equipping an AI assistant, the Antigravity CLI (`agy`) is available as a straightforward way to interact with the repository.

1. **Install gemma-dev skill:** Copy gemma-dev folder to your agent skill folder.

![Antigravity CLI skill](images/agy-skill.png)

2. **Start Your Session:** Launch an interactive Antigravity session by running `agy` in your terminal. From there, you can query the agent in plain English regarding the Gemma ecosystem. Since `agy` leverages the `gemma-dev` skill, you’ll receive the most precise and up-to-date technical guidance available.

![show me the chat template of gemma](images/agy-example01.png)
![show me the chat template of gemma (result)](images/agy-example02.png)

3. **Build Something Wonderful:** With your infrastructure handled autonomously, you can focus on the creative work. Turn on your favorite music, brew a fresh cup of coffee, and start creating!

# Building with Gemma Skills

> Example Prompt: `Build a smart home simulator using Gradio and Gemma, use direct voice input to Gemma to minimize the latency for controlling the home.`

![smart-home](images/agy-smart-home.png)
{{< youtube id="BAgLrR1_Ss0" >}}

Keep in mind that while the demo is functional, running a full-precision model via transformers can feel a little sluggish. For a better experience and optimal performance, I typically suggest serving a quantized version through a backend like *Ollama* or *LM Studio*, as shown in this next example.

> Example Prompt: `Build a terminal app that translates a user's natural language input into an ascii art animation, using Gemma and LM Studio backend.`

![ascii-ani app](images/agy-ascii-ani-app.gif)

I invite you to dive deeper into the vast world of Gemma and its surrounding ecosystem. You'll surely discover it’s an incredibly rewarding journey.

*Thank you for reading. If you build something cool with [`gemma-skills`](https://github.com/google-gemma/gemma-skills), let me know! Happy building!*

