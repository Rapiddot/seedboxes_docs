---
title: Why does my speed drop when I have many active torrents seeding?
id: why-speed-drop-many-active-torrents
description: Learn why your speed drops when you have many active torrents seeding and how to manage it effectively.
keywords:
    - speed drop
    - active torrents
    - seeding
    - BitTorrent
    - disk load
---
# Why does my speed drop when i have many active torrents

When you have many active torrents seeding at the same time you are loading your hard disk.

The most important bottleneck in BitTorrent is the disk load. The more torrents you seed, the more peers you are connected to. For each peer, you read/write at a random place on your disk. The more random accesses the disk has, the more its real speed goes down which in turn affects your total speed and reduces it.

You cannot have high speed by seeding many torrents. This is a choice you need to make. You either can have very high speed by seeding 1 or 2 very fresh torrents, or you can have moderate continuous speed seeding many torrents for a long time.

:::tip
When you have a fresh new torrent, what you can do, is to try and stop any other seeding torrent at that time temporarily in order to let your hard disk focus on that new torrent. The torrents seed a lot, only the first 1-2 hours of their life, so you can resume seeding all your other torrents after that again.
:::