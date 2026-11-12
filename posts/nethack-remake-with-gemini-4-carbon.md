---
canonical_url: https://bebechien.github.io/cozy-corner-future/posts/nethack-remake-with-gemini-4-carbon/
cover_image: images/nethack-remake-with-gemini-4-carbon.png
description: Learn how to remake the classic roguelike NetHack into a 3D action RPG
  using Gemini 4 Carbon and Blender MCP, complete with practical tips and process
  insights.
published: true
tags:
- Game
- Gemini
- Blender
- MCP
title: NetHack Remake with Gemini 4 Carbon
---
Hello everyone! Today, I’d like to share my experience testing out Gemini 4 Carbon. What did I build? I remade the classic 1987 retro roguelike game [NetHack](https://www.nethack.org/) into a modern 3D action RPG. The deep gameplay of the original dungeon crawler (originally rendered only in text and ASCII graphics) inspired countless games that followed, including Diablo, and thanks to its open-source nature, it continues to evolve to this day.

**✨ Remake Demo Promo Video**

{{< youtube id="4KfezQB4aW0" >}}

**Actual Gameplay Capture**

![NetHack 3D ARPG Remake](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-3d-arpg.gif)

Curious about how a text-based classic turned into a modern 3D action RPG? Follow along with the step-by-step guide below, and you'll be able to kick off your very own retro game remake project with ease!

# 🛠️ Prerequisites

- **Install Antigravity & Get Model Access:** Install the project development platform Antigravity, and secure access to the Gemini 4 Carbon model, which offers exceptional coding capabilities.
- **Set Up 3D Asset Automation Environment:** Install Blender for 3D modeling, add the MCP (Model Context Protocol) add-on, and connect the Blender MCP server to Antigravity.

> **📌 A Quick Note!** \
Public code repositories come with their own specific licensing terms. While you are generally free to experiment for personal learning, always check the project's license before using it commercially or sharing your final result publicly!

Now, let's go over the preparation steps one by one.

# 💻 Installing Antigravity & Accessing the Model

Install Antigravity - https://antigravity.google \
You can use Gemini 4 Carbon right away by subscribing to the [Google AI Ultra plan](https://one.google.com/about/google-ai-plans/).

Once you're all set up, create a new project in Antigravity and configure it to use Gemini 4 Carbon, as shown below.

![Antigravity Setup](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-1.png)

Shall we move on to the next step?

# 🎨 Setting Up 3D Asset Automation Environment

Why do we need a separate MCP server? Actually, you can develop 3D games using Carbon just fine without this setup. However, connecting MCP unlocks features specialized for 3D asset generation, resulting in a much more polished product. If you already use another server, feel free to use that; otherwise, follow the instructions below to connect the Blender MCP server.

Install Blender - https://www.blender.org \
Install Blender MCP Server - https://projects.blender.org/lab/blender_mcp/wiki/Setup \
Install Blender MCP Server Add-on - https://www.blender.org/lab/mcp-server/#add-on

Finally, to add the Blender MCP server to Antigravity, you need to edit the configuration file manually.

Click “Copy Config File Path” next to Customizations > Installed > MCP Servers, then open the file in your favorite text editor.

![Antigravity MCP Servers](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-2.png)
![Antigravity MCP Config](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-3.png)

In my case, because I already had the cloudrun MCP installed on Windows, my screen looks slightly different from yours. However, you can refer to the [official Wiki instructions](https://projects.blender.org/lab/blender_mcp/wiki/Setup#mcp-config-file) to add the settings for your specific environment.

After restarting Antigravity to load the updated config file, a green light will appear next to the blender entry as shown below. You’re now all set to start developing!

![Antigravity Blender MCP Connected](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-4.png)

# 🚀 Starting the Main Work

Once all preparations are complete, write a one-shot prompt to pass to the agent. Here is the actual prompt I used:

```text
/swarm Clone https://github.com/NetHack/NetHack and port it into modern web technology and wasm. Remake it into a 3D Action RPG. Use Blender MCP to generate high quality 3d assets.
```

![Antigravity Prompt](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-prompt.png)

Using the Swarm feature spawns subagents that process tasks in parallel. Instead of a single agent evaluating itself, independent agents with separate contexts objectively analyze each other's outputs, resulting in much higher-quality deliverables.

You can leave the permission settings at the bottom right to Default to require user approvals for key tasks, or set it to "Turbo" mode to let the agent work autonomously until final completion.

The execution time depends on the project size. While waiting, it’s fun to observe the agent’s reasoning process or monitor how tasks are being distributed in real time via the Swarm UI.

![Antigravity Swarm](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-swarm.png)

When all work is finished, Antigravity will display a notification. If there are areas you’d like to tweak, you can request additional revisions—or even ask for new features as fresh ideas come to mind!

# 🎁 Bonus: Adding Retro Vibes

Once your game implementation is rock solid, try creating a 1980s VHS-style promo video to add that extra retro charm!

```text
Create a promotion video with 80s vibe with VHS tape artifacts. Use Lyria 3.5 to generate background music. Use Gemini 3.8 Flash TTS to generate promotional messages.
```

Please note that for the agent to access the model in a local environment, you must either [set GEMINI_API_KEY](https://aistudio.google.com/docs/api-key) in advance or install the Gemini API plugin from Antigravity's Marketplace.

![Antigravity Plugin](https://bebechien.github.io/cozy-corner-future/images/nethack-agy-plugin.png)

And that covers the entire process of making the promo video shown earlier!

What kind of awesome project will you build next?