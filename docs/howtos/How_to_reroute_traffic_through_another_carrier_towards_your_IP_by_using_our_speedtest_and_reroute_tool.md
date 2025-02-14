---
id: how-to-reroute-traffic
title: How to Reroute Traffic Using Our Reroute Tool
description: Learn how to reroute traffic through another carrier towards your IP using our speedtest and reroute tool to improve your connection speed.
keywords:
    - reroute traffic
    - speedtest tool
    - improve connection speed
    - seedboxes.cc
    - ISP peering
---

# How to reroute traffic using our reroute tool

## Why someone might need the reroute tool
You might have noticed, that the speed that you can pull for our servers for downloading content via FTP to your home or for streaming through Plex, might fluctuate from time to time. This is not always caused because of a problem with your server. Actually, 99% of the time, your speed fluctuates because of bad peering between your ISP and our datacenter. This is because your ISP and us, are 2 different networks that need to be connected in a way in order to exchange traffic. 

In the case that we do have a direct connection with your ISP (through a private peering, or by directly interconnecting through an Internet Exchange), usually the peering is quite good, because there are not intermediate networks involved that can slow down the connection. In a manner, the connection is faster, because we reach your ISP's network in the most direct possible way, thus minimizing the posibility of bottlenecks or network errors along the way.

However, in many cases, in order to reach your ISP, we have to do it with other networks or carriers involved. In these cases, problems that might arrise in these intermediate networks might cause a slow down or increased latency. Also, both parties (us and your ISP) are paying these intermediate networks for access, in order to be able to reach other networks with them. Due to this fact, many ISPs, might not have the necessary capacity with these intermediate carriers, to sustain a high speed during their peak hours (usually evening hours) effectively causing their client's connections to be throttled in order to serve everyone through that carrier, in other words the ISP's ports with the intermediate carrier are congested.

For that reason, we are using multiple carriers for our network, in order to be able in most cases, to reach your ISP through many different paths and different intermediate carriers. This allows us to be redundant and at the same time provides the ability to reroute through them, if one of them is congested at some point.

So if you have noticed, that during specific times (in the evening for example) your speed is very slow compared to other times, you can try to reroute towards your ISP through other available options, that might provide better speed at that time.

## How can i reroute the connection towards my ISP

This tutorial will show you how to reroute your IP address from our speedtest service.

* First go to http://speedtest.seedboxes.cc and login with your seedboxes.cc account. This is necessary for you to be able to reroute your IP later.

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1512376821562.0.png)


* On the left you will see all of our available routes towards your ISP. The route in bold is your current route. If you enable the "Automatically Reroute" after the speedtest is done, the server will calculate the best route based on your results and apply it.


![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1512376938990.1.png)


* After the speedtest in finished you will be redirected to your results page. On the bottom of the results page is a table with the results of each route. You can reroute your IP just by clicking on the reroute button of the route you want to use. You can reroute your IP as many times as you want.


![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1512376956522.2.png)

    :::note
    You can request a reroute every 5 minutes. This is done to avoid abuse of our system.
    :::


![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1512376968737.3.png)


* And that's it. You are now using the route you selected.

:::info
The reroute will stay active for 7 days. After that, it gets deleted by our system. This is done because your IP address might change in that period, so there is no need for our system to keep the route.
:::

