# How to use Plex

The **Plex Media Server** is a closed source project, that is intended as a **home media center**, in order to stream your personal library. 

We support a dedicated plex server installation, meaning you will have administration access over your own plex server, and be able to change its settings at will.

## Plex Installation
First you need to create a [Plex.tv](https://www.plex.tv/) account if you already do not have one. It is **free** to create one.

* Login to your [client area](https://seedboxes.cc/client/dashboard).
    After you log in to your seedbox account, click in the **"My Client Area"** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491572428955.jpeg)

*  Under **"My Seedboxes"** click on the little gear icon next to the seedbox you want to use and click on the **"Manage Seedbox"** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491572473836.jpeg)

* Scroll down and Click on the **Installable Apps** Tab. Click on **"Add Application"**.From the application list, click on **"Plex Media Server"**, then click INSTALL.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491572902963.png)

* A popup emerges, which asks your **CLAIM CODE**. This is a code, which can be retrieved from [here](https://www.plex.tv/claim). This code, will link the newly installed Plex Media Server with your [Plex.tv](https://www.plex.tv/features/cloud/) username. This code expires 5 minutes after it is generated, so please make sure to use it immediately after it is generated and proceed with the Plex server installation.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491816935816.png)

* Once you click INSTALL, the installation will commence and you will be informed once it is completed.
* Once Plex is installed, you can click the "Go to Application" button to visit your new plex installation. Alternatively, you can go to https://plex.tv and after you login, to click the "Launch" Button on the top right corner of the screen. 
* Please login with your [Plex.tv](https://www.plex.tv/features/cloud/) account. Please be careful not to use your [seedboxes.cc](https://seedboxes.cc/) account to login, you need to **use the credentials of your** [Plex.tv](https://www.plex.tv/features/cloud/) **account** instead.

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
