---
id: how-the-internet-works
title: How the Internet Works
description: An in-depth explanation of how the internet works, including networks, peering, throttling, latency, and protocols.
keywords:
    - internet
    - networks
    - peering
    - throttling
    - latency
    - protocols
---
# How the internet works

Let's talk about networks. There are times where you are trying to download something from your Seedbox and the speed is just terrible or try to stream from Plex and it keeps buffering all the time. Other times you wonder why, even though you have a 1Gbp/s Fiber connection you can utialize only 10% of your available bandwidth and it just won't go faster. You might be thinking that there is something wrong with the server, 99% of the case is not.

This article will help you understand better how the internet works and what are the deciding factors for speed.

Let's start.

## Internet Networks

The Internet is a vast network made up of a collection of smaller networks. The networks that make up the Internet are connected in two main ways. Networks can connect with each other directly, in which case they are said to be “peered”, or they can connect via an intermediary network known as a “transit provider”.

At the core of the Internet are a handful of very large transit providers that all peer with one another. This group is known as Tier 1 network providers. Whether directly or indirectly, every ISP  around the world connects with one of these Tier 1 providers. And, since the Tier 1 providers are all interconnected themselves, from any point on the network you should be able to reach any other point. That's what makes the Internet the Internet: it’s a huge group of networks that are all interconnected.

There are two ways to directly peer with an other network. Public Peering and Private Peering.

### Private Peering

Private peering is the direct interconnection between only two networks, across a [Layer 1 or 2 link](https://en.wikipedia.org/wiki/Data_link_layer). The link is dedicated and is not shared with any other networks. That way the capacity between those two networks is guaranteed. Of course ISPs won't agree to peer for free.

### Public Peering

Public peering as the interconnection of 2 networks across a shared layer 2 network usually called an IX (Internet Exchange). You can think of an IX like a big network that is connected to a lot of switches. Unfortunatelly by connecting to an IX does not mean that you will be exchanging traffic with all of the other participants of the IX. To peer with an other network you have to mutually agree to it. Many network, mostly ISPs have a selective or closed peering policy. That means that won't peer with just anyone. This increases the chances to sign private peering agreements.

The Amsterdam Internet Exchange (AMS-IX), Frankfurt Internet Exchange (DE-CIX), and the London Internet Exchange (LINX) are three of the largest exchanges in the world. 

Of course most networks are connected to more than one transit and Internet Exchange, making that network redundunt to network malfunctions since a network can be reached through many providers. So, how does a router choose the route to reach a network? 

The routers choose the route with fewer intermediary networks. Most of the time the fewer networks are between the source and the destination the better. But there are times that the shorter route is not the best option due to a congestion or a network malfunction of an intermediary hop (router). Unfortunately routers can't detect congestions so they can't reroute traffic to an other available path.

So as an example imagine you are in Netherlands and you want visit Germany for the holidays. There are many possible routes to take to reach your destination. You can go directly to Germany since it's a neighboring country or go through Belgium. But as you know traffic can be unpredictable. The shortest route is not always the fastest. A car accident or high demand during holidays might create a traffic jam to the shortest route, so taking the long route might be faster.

The same thing happens with networks. During prime hours (mostly evenings) and weekends, high bandwidth demand like Music and Video streaming, Gaming etc. can cripple the ISP's network. To avoid that, ISPs use bandwith throttling. 


## Throttling

Let's make something clear. All ISPs throttle their customers connections at some point and on most of the cases that is quite normal. The capacity an ISP has is not infinite and certainly is lower than the total bandwidth it's selling to it's customers. They usally play a game of average because the chances of all of their users trying to use all of their bandwidth at the same time are slim to none.

ISPs that saying they don't throttle their users connections will actually throttle bandwidth during certain times of the day to decrease congestion over their network, which saves them from buying more bandwidth from IP transits and more and faster equipment to handle internet traffic at that level.

Thottling vary from ISP to ISP. Some ISPs throttle connection to certain protocols such as FTP or HTTP, others throttle users who download heavy amounts of data or exceeded their monthly cap.

There have been case where ISPs have been accused of deliberately throttling traffic to networks ultimately leading to signing private peering agreements with the network.

Unfortunately there is no way to prove that your ISP is throttling your connections and that is why most of the time they won't admit it.

## Latency

Now, in cases that there is no throttling involved, let's see why you can't get full speed when you are download from certain networks. We get a lot of tickets from users saying that they switched from 100 Mbp/s to a 1 Gbp/s fiber connection and they can't get more than 15 - 20 MB/s when downloading from their seedbox, and that is perfectly normal. That is most likelly to be the maximum speed you can get on a single tcp connection. The reason for that is latency.

Most of the applications you use like browsers, FTP clients, Plex use the TCP protocol to communicate and exchange data. The TCP protocol or else called the reliable protocol provides reliable, ordered, and error-checked delivery of data and the way the tcp protocol works is that for every "n" number of packets (tcp window) the server sends to the client it expects an acknowledge response from the client that it received the packets without any problems. If the server does not get the response in a certain amount of time then it retransits the packets to the client.

So the greater the latency the longer it takes for the server to receive the acknowledgement response from the client to start sending the next batch of packets. Of course you can open multiple tcp connections to the same server and increase the amount of data your receive overtime.

Let me give an example. You have to load 100 boxes (server) to a truck (client). The truck is 10 meters away from the boxes and it takes 10 seconds (round trip latency) to walk to and back from the truck. You can carry 5 boxes (tcp window) at a time. This will take you (100 / 5) * 10 = 200 seconds to move all the boxes to the truck. Now let's move the truck 10 meters further. The latency is doubled and also the total amount of time it takes you to move the boxes. If the way to the trunk is wide enough (bandwidth) you can have a coworker (2nd tcp connection) moving boxes with you simultaneously. This will cut transfer time in half.

So depending on the latency, by increasing the bandwidth of your connection won't necessarily increase the speed you download from a network. It will increase the number of concurrent connections you can open on separate networks without one affecting the other, meaning, you could download while streaming netflix and fill up your whole line.

## Protocols

I am sure you heard of the terms FTP, HTTP, SSH before. Those protocols among others are build on top of the TCP protocol and each protocol is designed for different uses even if all of them in the end do the same thing, transfer data. You can transfer a file from a server to your home computer using HTTP, FTP and SSH (SFTP) right? But the performance will be different for each protocol as each protocol has it's pros and cons.

For example FTP is faster than SFTP (SSH File Transfer). FTP (File Transfer Protocol) as the name implies is designed to transfer files and nothing more. Is a very lean and comparatively simple protocol with almost no data transfer overhead, while SFTP is using SSH tunnels to transfer the data and SSH was designed as a replacement for Telnet and other insecure remote shells, not for very high speed communications.

An other example is file syncing. If you ever used Rysilio Sync or Syncthing (available on our installable apps) you will see that the overall speed for the initial sync of a folder will be lower than transfering the folder via FTP. Both of those technologies compared to FTP/SFTP uses a lot of CPU to segment, hash and encrypt/decrypt the data every time new files or changes are detected. This way it can detect changes and transfer only those pieces to the other endpoints, so if you change a big file it will not transfer the whole file again but only the chunks that changed. FTP on the other hand will have to transfer the whole file again to apply the changes. 

So depending on what you need you might have to use different protocols / applications.

## Conclusion

As you can see there are many things that can affect your speed. To help you in case there is a peering problem between our Datacenter and your ISP we created our Speedtest / Rouroute tool so you can diagnose and solve peering problems as fast as possible. You can read more on how to use it here: [How to reroute traffic through another carrier towards your IP by using our speedtest and reroute tool](./How_to_reroute_traffic_through_another_carrier_towards_your_IP_by_using_our_speedtest_and_reroute_tool.md)

For anything else you can always open a ticket so we can help you as best possible... :-)

:::info See also
* [Peering](https://en.wikipedia.org/wiki/Peering)
* [Bandwidth throttling](https://en.wikipedia.org/wiki/Bandwidth_throttling)
* [Level 3 accuses six broadband providers of degrading network traffic](https://www.cnet.com/news/level-3-accuses-six-broadband-providers-of-degrading-network-traffic/)
* [Syncthing - Why is the sync so slow](https://docs.syncthing.net/users/faq.html#why-is-the-sync-so-slow)
:::