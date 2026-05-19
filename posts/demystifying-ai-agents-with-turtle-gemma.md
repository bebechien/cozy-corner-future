---
canonical_url: https://bebechien.github.io/cozy-corner-future/posts/demystifying-ai-agents-with-turtle-gemma/
cover_image: images/demystifying-ai-agents-with-turtle-gemma.png
description: ''
published: true
tags:
- Turtle
- Gemma
- AI
- Agent
title: Demystifying AI Agents with Turtle & Gemma
---
# 🐢 Speaking into Canvas

If you're anything like me, your very first taste of "programming" might have involved a tiny triangle on a glowing CRT monitor. You typed `FORWARD 100` and watched as the little turtle drew a line across the screen. It was pure magic. You were making the computer do things. (See also: [Logo (programming language)](https://en.wikipedia.org/wiki/Logo_(programming_language)))

Recently, I rediscovered this magic with AI, a project called [Turtle-Gemma](https://github.com/bebechien/turtle-gemma), and it brings that exact childhood magic to the modern AI landscape.

Instead of typing commands, you just click a microphone in your browser and say, "Hey, draw me a red star." A few moments later, an AI agent writes the Logo code, executes it, and paints your request onto a digital canvas.

![turtle gemma screenshot](https://github.com/bebechien/turtle-gemma/raw/main/screenshot.png)

It was a fun tinker project, but it’s also something more: it is one of the most effective way to understand how modern AI "Agents" actually work. Let's peek under the shell.

# 🛠️ Gluing It All Together

There’s a special kind of satisfaction in taking a handful of different technologies and wiring them together into a seamless loop. That’s exactly what Turtle-Gemma does.

If you look at the architecture, it’s a beautifully simple pipeline:

1. **The Ears:** A Gradio web interface captures your voice or text request.
2. **The Brain:** Google’s Gemma model takes that input and acts as an agent.
3. **The Hands:** A custom-built, "headless" turtle engine (`turtle_engine.py`) takes the agent's instructions and draws them onto a PIL (Python Imaging Library) image.

As a maker, I love this. It’s a reminder that you don't need a massive enterprise stack to build something that feels futuristic. A clean Python environment, an open-weights model, and a simple UI library are all you need to go from a spoken thought to a rendered image.

# 💭 Demystifying "Tool Calling" by Watching the AI Think

If you’ve been hanging around the AI space recently, you’ve probably heard the terms "Agentic Workflows" or "Tool Calling." They sound heavy and intimidating. Usually, they describe an AI querying a database, parsing JSON, or fetching weather APIs—tasks that are powerful, but practically invisible.

Turtle-Gemma is the perfect cozy visualizer for tool-calling.

When you ask Gemma to "draw a red star," the model doesn't just output a raw image file. It has to *think* about the steps required and use the "tools" it was given. In this case, those tools are literally just `move_turtle()`, `turn_turtle()`, `set_pen_state()`, and `set_pen_color()` (Ref: [turtle-gemma/config.py](https://github.com/bebechien/turtle-gemma/blob/main/config.py)).

You get to watch the AI reason out loud:

* *"The user wants to draw a red star using turtle graphics. A star is a polygon, typically drawn by moving forward and turning a specific angle repeatedly."*
* *Tool Call 1: `set_pen_color("red")`*
* *Tool Call 2: `move_turtle(100)`*
* *Tool Call 3: `turn_turtle(144)`*
* *(Repeats 5 times)*

By forcing the LLM to output physical, sequential steps on a canvas, the abstract "black box" of AI reasoning becomes entirely visual. If the AI hallucinates or messes up its logic, you don't get a silent code crash—you get a weird, lopsided star instead of a perfect one. You are literally watching the model think in real-time.

# 😋 Embracing the Happy Accidents

Of course, because this is an AI trying to navigate a 2D space, things don't always go perfectly—and that’s part of the fun.

Prompt: `draw a x-mas tree`

![x-mas tree](https://bebechien.github.io/cozy-corner-future/images/x-mas-tree.png)

Sometimes you’ll ask for a x-mas tree, and the AI will forget to draw the trunk, resulting in a wonky triangle with a single green line shooting out the bottom. Other times, it might get slightly confused about its current heading and draw odd lines.

These little "mistakes" are incredibly endearing. They remind us that LLMs aren't infallible magic brains; they are reasoning engines doing their best to map language to geometry.

# 🏖️ Go Play in the Sandbox

We spend so much time using AI for serious tasks—writing emails, debugging servers, or parsing spreadsheets. Turtle-Gemma is a wonderful reminder that programming with AI can still just be about *play*.

Prompt: `draw a gangnam style`

![Gangnam Style](https://bebechien.github.io/cozy-corner-future/images/gangnam-style.png)

If you want to see tool-calling in action, or if you just want to experience the joy of speaking a shape into existence, I highly recommend cloning [the repo](https://github.com/bebechien/turtle-gemma), spinning up the Gradio app, and giving it a try.

Go tell the turtle to draw a star. It might just make you smile.