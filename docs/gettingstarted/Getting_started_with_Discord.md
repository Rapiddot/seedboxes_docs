---
id: getting-started-with-discord
title: Getting started with Discord
description: A comprehensive guide on how tp install Discord and link it to your Seedboxes.cc account.
keywords: [discord, seedbox, client area, settings]
---

# Getting Started with Discord

Our Seedboxes.cc community has moved to **Discord** — a modern communication platform that allows us to provide faster support, direct interaction, and new features such as account-linked bots and AI helpers. This guide will walk you through the basics of using Discord and linking your account.

## What is Discord?

Discord is a free application for chat, voice, and community interaction. It’s widely used by gaming, tech, and open-source communities, and now serves as the home of our Seedboxes.cc community.  
With Discord, you can:

- Chat with other members in real time  
- Receive support directly from our team  
- Access our Seedboxes.cc bot to perform account actions  
- Ask questions to our AI support bot  
- Use the Seedbox Bot to perform actions and see the status of your seedbox.

## How to Download Discord

Discord is available on multiple platforms:

- **Windows / macOS / Linux:** [Download Discord for Desktop](https://discord.com/download)  
- **iOS / Android:** Search for **Discord** in the App Store or Google Play Store  
- **Web Browser:** Access directly via [discord.com](https://discord.com)

Once installed, create a free Discord account (if you don’t already have one).

## Linking Discord with Your Seedboxes.cc Account

To get the right permissions and access all features in our Discord server, you’ll need to link your Seedboxes.cc account with Discord:

1. Log in to your [Seedboxes.cc Client Area](https://www.seedboxes.cc/client/settings).  
2. Go to **Settings** in your account.  
3. In the **Discord** section, click **Link Discord**.  

![](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/f9011f1f-6595-49ef-9b21-20a0da242a60.png)

4. Authorize the connection when prompted by Discord.  
5. Once linked, you can click on the "Join our Discord" button, to get an invitation and join our Discord Channel.  

:::tip Linking ensures you’re assigned the correct member role and can use our support bots effectively.
:::

## Joining the Server

After linking your account, click on your personal invitation link from the Settings page. This will open the Discord app and join you to the official **Seedboxes.cc Discord Community**.

From there, you can:  
- Introduce yourself in the **#main-chat** channel  
- Ask questions in **#support**  
- Share feedback or ideas in **#feedback-ideas**  
- Stay updated through our **#status** announcements  

🎉 That’s it! You’re now ready to enjoy our new Discord community with better support, automation, and a more engaging environment.

## Using the Seedboxes.cc Discord Bot

Our custom bot allows you to manage your seedbox directly from Discord. Below are the available commands:

### General Commands
- `/help` — Show the list of available commands.  
- `/syncroles` — Refreshes your Discord roles to match your Seedboxes.cc account. You can use this if for some reason your role is not applied automatically from the bot. Make sure you have linked your Discord to your Seedboxes.cc account first.

### Account Management
- `/account status` — Displays your account email, credit balance, recent invoices, and active seedboxes.

### Seedbox Management
- `/seedbox status <username>` — Shows the plan, server, disk usage, traffic, and installed apps for your seedbox.
- `/seedbox restart_torrent_client <username>` — Restarts the torrent client on your seedbox.
- `/seedbox change_torrent_client <username> <new_client>` — Switches to a different torrent client (pick from the list shown by Discord).
- `/seedbox app <username> <action> <app>` — Installs, uninstalls, stops, or restarts one-click apps on your seedbox. Some apps (like Plex or JDownloader) may ask for extra info in a pop-up.
- `/seedbox reclaim_plex <username> <plex_claim_code>` — Applies a new Plex claim code for the Plex app on your seedbox.

### Support & AI Agent
- `/ask <question>` — Sends a support question to our automation assistant and replies with the answer. The AI Bot will search our official documentation and provide guidance.

:::info
Most commands only work if you’re a subscribed member and target seedboxes you own. In this case, you should have a "Member" role in discord. Make sure you have linked your Discord account, in order to get the "Member" role automatically. 
:::