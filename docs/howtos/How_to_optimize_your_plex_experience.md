---
id: optimize-plex-experience
title: How to Optimize Your Plex Experience
description: Learn how to optimize your Plex experience by configuring your Plex clients and settings for the best streaming performance.
keywords:
    - Plex
    - Plex optimization
    - Plex streaming
    - Plex clients
    - Plex Media Player
    - 4K streaming
    - media server
---

# How to optimize your plex experience

## Introduction
By installing the plex app at your seedbox, you are creating a new plex server at your plex account in which the remote media will reside and ready to be streamed.

However, the plex client is the one responsible for requesting content by sending the plex server the necessary information regarding whether the resolution and video/audio codecs are supported or not. If the plex client fully supports those, the content is directly streamed from the server, resulting in faster loading times and no buffering/pauses due to processing during the stream.

If the plex client doesn't support the content's resolution or codecs for direct streaming, it sends the plex media server a request for transcoding (meaning "something which can understand" so it can stream it), which results in a heavily-dependent cpu process that causes slow starting times and might cause buffering in some cases. If too much transcoded is needed to be done and the server is not powerful enough, then the stream pauses (resulting in buffering) until the server is ready to send the next transcoded/processed "chunk" for streaming towards the plex client.
This is the reason why a Bat Box is not powerful enough to stream 4K transcoded content, yet it suffices for direct 4K streaming, if supported by the plex client.

In other words, you should aim having a plex client that natively supports as many formats and codecs as possible.

## Plex clients
There are several plex clients [available](https://www.plex.tv/apps-devices/), depending on your device.
For example, there are plex web app players, TV (Smart/Android) based plex clients, gaming console (Xbox, PS, Nvidia Shield) plex clients as well as streaming devices such as Chromecast, Apple TV, Amazon Fire TV Stick, or Roku that support the installation of a plex client.
And of course, there is the **Plex Media Player**, a dedicated player by Plex itself, which will see later on.

Most users stream via their browser or via their TV based plex client. This is, unfortunately, **not optimum**.
Web browsers don't support all media formats and codecs, resulting in content being transcoded in order to be streamed.
So unless you stream content that is strictly up to 1080p, mp4 container with h264 video codec and aac audio codec, then you need to change your streaming habits to ensure the best experience available.
The same goes for TV's too, plus they are not that actively supported - unless of course you own a state-of-the-art and/or recent TV. As stated at the official plex [page](https://support.plex.tv/articles/204080173-which-smart-tv-models-are-supported/) regarding TV support and especially older TV's, *"Since these platforms and models are no longer supported, we encourage users to instead make use of a modern Plex app on a supported platform. For instance, we have Plex apps available on Roku, Chromecast, Apple TV, Fire TV, Android TV, game consoles, etc."*

You guessed right, getting a special device, like a Roku or Chromecast, will fully boost your streaming experience. Plus it will make your smart TV even smarter :)

As for using your PC web browser for streaming, there is a better alternative; Plex offers the [Plex Media Player](https://www.plex.tv/blog/introducing-the-plex-media-player/) (*tip:* it no longer requires a plex pass) which delivers *"the absolute highest quality media browsing and playback experience"*.
Having a dedicated app, based on the best media player engine (mpv) that is solely built for this purpose, is obviously going to be a better solution than streaming from a browser.

But what about tinkering settings in Plex Media Player (and generally, plex clients) to ensure that you get the most out of it?

### Plex Media Player settings

It really comes down to the **"Video"** settings. Just make sure that every type of quality (**local/remote/online**) and especially "remote" is set to **Original**. Otherwise, if you have set a forced resolution, it will always start the stream at that resolution by transcoding it first.
Also, enable the **Hardware Decoding** and make sure that the **Allow Direct Play** and **Allow Direct Stream** are also enabled.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1613407888348.png)

Finally, head to the **"Audio"** settings. You probably want the **Basic** device type, the **Auto Select Channels**, the **Built-in Audio Analog Stereo** and the **Normalize Downmixed Volume**. These options are valid for most users streaming at their PC without any special gear. You can of course change those settings based on your hardware configuration, you can find more info regarding the audio settings [here](https://support.plex.tv/articles/audio-configuration/).
For example, if you plug your PC at a home theater system with a 5.1 surround sound setup, make sure to change the settings accordingly (device to HDMI or optical if you use one, Channels to 5.1 etc).

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1613409726440.png)

### Direct 4K TV playback

Having a 4K TV, doesn't mean you can directly stream content via its plex client. You need to make sure that the media format (container and codecs) you wish to directly stream is **fully** supported by the manufacturer. Else, you will be needing at least the Vampire box for streaming transcoded 4K content (regular bitrate) or the Zombie box for transcoded 4K content with very high video bitrate.
*Note:* Most TV plex clients **don't support** native 4K streaming for the majority of 4K downloaded content.

In that case, you can purchase a device that supports a very large range of formats for native 4K streaming such as an Nvidia Shield. Chromecast or Roku are also an option (and way cheaper too) but are less compatible with all the audio codecs. It really comes down to what content you already have or about to download - just get the device that is compatible to that.
*Tip:* Make sure you connect your device to your router via ethernet. You should *really* avoid streaming 4K via wifi. It would be a pity to set everything up, only to discover that your internal (local) network is causing you bandwidth or connectivity issues.

Finally, don't forget that you need to have a very fast network for 4K streaming (regardless of direct or transcoded streaming). You should run our [speedtest](https://speedtest.seedboxes.cc/) during evening times where the ISP's have more chances to be congested. For regular 4K video bitrate, you should get at least 40-50MBps at the "Average" column. You can find more info regarding our speedtest tool and how to reroute traffic in order to achive better network speeds [here](https://community.seedboxes.cc/articles/how-to-reroute-traffic-through-another-carrier-towards-your-ip-by-using-our-speedtest-and-reroute-tool)