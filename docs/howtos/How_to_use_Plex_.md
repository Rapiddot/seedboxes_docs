---
id: how-to-use-plex
title: How to use Plex
description: Learn how to install and use Plex Media Server on your seedbox to stream your personal media library. Follow our step-by-step guide for a seamless setup.
keywords:
    - Plex
    - Plex Media Server
    - seedbox
    - media streaming
    - home media center
    - Plex installation
    - streaming setup
---

# How to use Plex

The **Plex Media Server** is a closed source project, that is intended as a **home media center**, in order to stream your personal library. 

We support a dedicated plex server installation, meaning you will have administration access over your own plex server, and be able to change its settings at will.

## Plex Installation
First you need to create a [Plex.tv](https://www.plex.tv/) account if you already do not have one. It is **free** to create one.

* Login to your [client area](https://seedboxes.cc/client/dashboard).
    After you log in to your seedbox account, click in the **"My Client Area"** button.

![file](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/a26847ea-a04d-4fe9-b283-ecb5108404b3.png)

* In your dashboard, select the seedbox where you want to install Plex.

![client_area_select seedbox.png](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/a7d33c23-234c-47af-aaa0-68b39f72a763.png)

* Select the **"Apps"** Section. Find "Plex" in the "Available Applications" list, and click to install it.

![plex_install.png](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/70a30fb3-224b-4dcf-b1a5-0a6d55a52120.png)

* A popup emerges, which asks your **CLAIM CODE**. This is a code, which can be retrieved from [here](https://www.plex.tv/claim). This code, will link the newly installed Plex Media Server with your [Plex.tv](https://www.plex.tv/features/cloud/) username. This code expires 5 minutes after it is generated, so please make sure to use it immediately after it is generated and proceed with the Plex server installation.

![plex_claim.png](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/5229ce05-281b-4fd6-ac5e-f30d97d2f844.png)

* Once you click "Continue Install", the installation will commence and you will be informed once it is completed.
* Once Plex is installed, you can click the "Go to App" button to visit your new plex installation. Alternatively, you can go to https://plex.tv and after you login, to click the "Open Plex" Button on the top right corner of the screen. 

* The setup is now completed. Our automated installer should have created 3 default libraries for you (Movies, TV and Music). You can create as many other libraries as you want of course.

## Streaming with Plex

:::warning Important
To stream your media files you will need to move your media files inside the appropriate Plex directory! Please try to avoid to point your ~/files/downloads folder as your Movies and TV path in your libraries. If you do this, your plex server will underperform during scanning of new media, will make many wrong matches, and potential crash often.
:::

**Moving your files with ruTorrent**

If you want **to continue seeding the files** and move them, then the correct way to do this is:

* Right click the release on your ruTorrent
* Select "Save To..."
* Choose the folder where you want to move the release, and make sure the options "Move Data Files" and "Fast Resume" are checked
* After you click OK, ruTorrent will move your data files and resume seeding your release

If you **do not want to continue seeding the files** you can easily move them via the **File Manager** which your ruTorrent provides (look at the tabs at the bottom).

**Moving your files with FTP**

If you are not using ruTorrent as your torrent client, then the only alternative is to use an FTP client (such as FileZilla) and move the files you want in the appropriate Plex directories.
