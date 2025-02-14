---
id: how-to-use-your-media-player-with-your-remote-mount
title: How to Use Your Media Player with Your Remote Mount
description: Learn how to use Plex, Jellyfin, or Emby with your remote mount to access your cloud media on your seedbox.
keywords:
  - Plex
  - Jellyfin
  - Emby
  - remote mount
  - seedbox
  - cloud media
  - media player
---

# How to use your media player with your remote mount

## Introduction

You have installed either a plex media server, jellyfin or emby via [1-click installable apps](./How_to_install_our_1-Click_applications.md), and you would like to use the Google or Dropbox drive (or a crypt drive that is based on such drives) to those apps too, so you can access your existing cloud media!
This is now doable! Just create a [remote mount point](./How_to_mount_a_remote_drive_to_your_seedbox.md) via your seedbucket and once the process is finished, the mount becomes available!

## Plex

Once you finish the plex installation via your client area, head to [https://app.plex.tv](https://app.plex.tv) . There, you will find your seedbox plex server that you just installed.

In order to add the cloud content to your plex server via Libraries, you need to edit the corresponding library and add that content.

For example, for your TV shows, just click the **three dots**, select **Manage Library** and then the **Edit...** from the menu.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639741275536.PNG)

A modal will open directly at the TV Shows section. Just click the **Add folders** to the left.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639741564252.PNG)

The added paths for those folders will appear here. The seedbox Plex folders are already added for you. You just need to add the cloud folders via your remote point that you mounted earlier. Click the **BROWSE FOR MEDIA FOLDER** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639741592323.PNG)

Navigate to **/home/user/mounts/rclone/**  and you will find the content there.
:::note
If you own a Vampire or better tier seedbox, you can mount two remote points. The second can be found at **/home/user/mounts/rclone2/** .
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639741658325.PNG)

Navigate to the correct subfolder for that media type (e.g. /home/user/mounts/rclone/media/TV Shows) and once ready, click the **ADD** button so new content is added. Save the changes at the end.

Do the process again for every category you have (e.g. Movies) and plex will automatically scan new content.
**Note:** Depending on the size of that cloud content, the scan process can take a while to finish!

That was it! Enjoy streaming your cloud content!

## Jellyfin
Once you finish the Jellyfin installation via your client area, visit the app via the link **"Go to application"** (which is essentially https://USERNAME-jellyfin.cloud.seedboxes.cc/ ) . After logging in with your seedbox credentials, click the **user** icon at the top right corner of your screen.

The settings page will open. Click at the **Dashboard** link under the **Admin**.
At the left section of the screen, click the **"Library** link under the **Server** settings.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639752559297.PNG)

You can create as many libraries as you want. For example, you can create one for your Movies, one for your Shows, one for your Music etc. The local seedbox paths for them can be set anywhere you want, e.g. "/home/user/files/Media/". 
In order to add your cloud content via the mount point into them, just click the corresponding library and add the remote mount path.

For example, for the "Shows", a new modal will open in which you can add a new path by clicking the **"+"** button next to the Folders.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639752625101.PNG)

Navigate to **/home/user/mounts/rclone/**  and you will find the content there.
**Note:** If you own a Vampire or better tier seedbox, you can mount two remote points. The second can be found at **/home/user/mounts/rclone2/**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639752659561.PNG)

Navigate to the correct subfolder for that media type (e.g. /home/user/mounts/rclone/media/TV Shows) and once ready, click the **Ok** button at the bottom so new content is added. Press esc to close the modal. If the scan doesn't automatically start, you can right click at the category, select the **Refresh Metadata** button and finally the **Refresh** button at the new modal.

Do the process again for every category you have (e.g. Movies) and Jellyfin will automatically scan new content.
**Note:** Depending on the size of that cloud content, the scan process can take a while to finish!

That was it! Enjoy streaming your cloud content!

## Emby
Once you finish the Emby installation via your client area, visit the app via the link **"Go to application"** (which is essentially https://USERNAME-emby.cloud.seedboxes.cc/ ) . After logging in with your seedbox credentials, click the **gear** icon at the top right corner of your screen.

The settings page will open. At the left section of the screen, click the **"Library** link under the **Server** settings.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639751062104.PNG)

You can create as many libraries as you want. For example, you can create one for your Movies, one for your TV Shows, one for your Music etc. The local seedbox paths for them can be set anywhere you want, e.g. "/home/user/files/Media/". 
In order to add your cloud content via the mount point into them, just click the corresponding library and add the remote mount path.

For example, for the "TV Shows", a new modal will open in which you can add a new path by clicking the **"+"** button next to the Folders.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639751324291.PNG)

Navigate to **/home/user/mounts/rclone/**  and you will find the content there.
**Note:** If you own a Vampire or better tier seedbox, you can mount two remote points. The second can be found at **/home/user/mounts/rclone2/**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639751404889.PNG)

Navigate to the correct subfolder for that media type (e.g. /home/user/mounts/rclone/media/TV Shows) and once ready, click the **Ok** button at the bottom so new content is added. Press esc to close the modal. If the scan doesn't automatically start, you can right click at the category and select the **Scan Library Files** button.

Do the process again for every category you have (e.g. Movies) and Emby will automatically scan new content.
**Note:** Depending on the size of that cloud content, the scan process can take a while to finish!

That was it! Enjoy streaming your cloud content!

### Emby apps / devices
You can connect your seedbox server you just added by inputting the following host/port settings to any Emby App or Device (client) :

> host: https://myusername-emby.cloud.seedboxes.cc
> port: 443

  (substitute "myusername" with your seedbox username)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640077741198.PNG)

At the next screen, login with your seedbox credentials and you should have access to your Emby seedbox server via your Emby client