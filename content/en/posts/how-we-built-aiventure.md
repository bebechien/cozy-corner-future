+++
title = "How we built AIventure, an AI-Powered Retro Dungeon"
date = "2026-06-10"
cover = "images/how-we-built-aiventure.png"
tags = ["Game Dev", "Gemini", "Gemma", "AI"]
description = ""
showFullContent = false
readingTime = false
hideComments = false
+++

Grab a refreshing slice of cold watermelon (because it’s summer in Tokyo and I love it!), and let me tell you a story about how a small team of us turned a wild idea into a living, breathing web game.

If you’ve spent any time in Google I/O over the last few years, you might remember *[Adventure](https://www.youtube.com/watch?v=hMjtFRqaTsI)*—the virtual conference technology that powered major Google events during the pandemic. It was vast, beautifully illustrated, and collaborative. But it was also heavy, transient, and required an army of human moderators.

{{< youtube id="hMjtFRqaTsI" >}}

A few months ago, I and Tom started asking ourselves a question: *What if we re-imagine Adventure?* Instead of a one-off conference, what if we build a cozy, retro persistent world that teach developers the principles of Generative AI not through dry documentation, but through **"vibe coding"** and gameplay?

![aiventure](images/aiventure.png)

That was the spark for **[AIventure](https://developers.google.com/solutions/learn/aiventure)**. Here is the tale of how we actually built it.

# Step 1: Scribbles and Prototyping in Gemini Canvas

Every good game starts with a prototype. For AIventure, we didn’t start by writing complex engine code. We started by playing around with concepts inside Gemini.

We knew we want a split UI layout: a high-quality frontend framework (**Angular**) to manage the UI panels and layout, wrapped around a retro canvas powered by **Phaser.JS** for the actual game engine. This is the same approach we did for our previous I/O demo, the "[Living Canvas](https://developers.google.com/solutions/learn/living-canvas)".

We first built a simple educational puzzle game using various styles. We eventually landed on a top-down retro dungeon approach because it just felt right for the "vibe" we wanted. It was at this point that Tom brought in the brilliant idea of reviving the spirit and aesthetics of his previous project, "Adventure," to give the world its cohesive identity.

> Screenshots of Initial prototypes in [Gemini Canvas](https://gemini.google/overview/canvas/)

![screenshot01](images/aiventure-prototype-1.png)
![screenshot02](images/aiventure-prototype-2.png)

# Step 2: Designing the Rooms (Vibe Coding & Agentic Robots)

Once we knew the foundational logic worked, Tom and I began brainstorming more advanced puzzle mechanics. We didn't want the AI to just act as a lock-and-key mechanism; we wanted to showcase what makes modern LLMs so magical.

That led to two of our favorite creations:

1. **The Vibe Coding Room:** We wanted to introduce players to the concept of AI-assisted UI design. In this room, the game opens an iFrame tab. The player gives prompts like, *"build a todo app for the chicken that only have eat and sleep buttons"*. The AI builds a web page on the fly, and the player can immediately see their code and update inside the game environment.

![vibe coding room](images/aiventure-vibe-coding-room.png)

2. **The Agent Puzzle:** We introduced a little robot NPC character that accepts natural language instructions and executes them inside the Phaser grid world. If a player says, *"Go flip the switch"* then the model uses tool-calling and reasoning to break the instruction down into concrete, step-by-step game actions.

![agent puzzle](images/aiventure-agent-puzzle.png)

# Step 3: From Gemini to Gemma

During our initial build and testing phases, we relied on cloud endpoints—specifically pushing prompt requests out to Gemini models via Gemini API to handle player commands and code generation. It worked flawlessly, but we wanted to push the boundaries of what a modern web app could do. We wanted this game to be entirely self-contained and accessible.

Enter **[Gemma 4](https://deepmind.google/models/gemma/)**.

We began testing the puzzles with Gemma 4 models. We experimented with different sizes (E2B and E4B) and frameworks, including Ollama, LM Studio, Transformers, and Vertex AI, tracking how well the model could handle function-calling and agentic workflows.

# Step 4: Bringing it All to the Browser with MediaPipe

The final piece of the puzzle was deployment. How do we share an AI-powered game with millions of developers on the Google Developers site without forcing them to configure cloud backend architectures or input private API keys?

The answer lay in running the model **locally, right inside the user's browser**.

We used **MediaPipe** and the LiteRT team's [pre-converted formats](https://huggingface.co/litert-community/gemma-4-E4B-it-litert-lm) to host and serve the model distribution right from the website interface. By utilizing client-side web technologies, the entire experience runs locally on your machine. When a player prompts an NPC or writes code in the game, the inference happens entirely client-side. The frontend routes the request through a simple Event Bus directly to the browser-loaded model.

For developers exploring the source code at home, we built [toggles](https://github.com/bebechien/AIventure/blob/main/src/app/app.config.ts) so you can easily point the same game loop to a locally hosted LM Studio endpoint or [Vertex AI](https://github.com/bebechien/AIventure/blob/main/python-llm-service/main.py)!.

# One more thing…

In addition to our current puzzles, we are exploring the multimodal capabilities of Gemma. Although this work is currently in progress, you can experiment with it yourself by cloning our [GitHub repository](https://github.com/bebechien/AIventure).

![draw puzzle](images/aiventure-draw-puzzle.png)

# What Will You Create Next?

Building AIventure was a journey of bridging old-school game design with modern client-side AI. Seeing a retro game talk to a local open LLM to vibe code inside a dungeon puzzle still feels like magic to us.

We’ve published the demo, complete with developer profile badges to unlock along the way. If you want to check out the solution, inspect our full architecture, or look through our prompts, you can explore the official page right here:

👉 [Check out the AIventure Solution](https://developers.google.com/solutions/learn/aiventure)

Grab your sword, open up your console, and happy building! 🍉🎮

