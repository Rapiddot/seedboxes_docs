# How to use Sonarr and Radarr with your remote mount

## Introduction

You have installed sonarr and/or radarr via [1-click installable apps](./How_to_install_our_1-Click_applications.md), and you would like to use the Google or Dropbox drive (or a crypt drive that is based on such drives) to those apps too, so you can access your existing cloud media!
This is now doable! Just create a [remote mount point](./How_to_mount_a_remote_drive_to_your_seedbox.md) via your seedbucket and once the process is finished, the mount becomes available!

## Sonarr
Once you finish the sonarr installation via your client area, visit the app via the link **"Go to application"** (which is essentially https://USERNAME-sonarr.cloud.seedboxes.cc/ ) . After logging in with your seedbox credentials, click the **Import Existing Series** button at the viewscreen.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640013635587.PNG)

At the new screen, click the only button available - **Start Import**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640017280321.PNG)

At the new modal, navigate to **/home/user/mounts/rclone/**  and you will find the content there.

:::note
If you own a Vampire or better tier seedbox, you can mount two remote points. The second can be found at **/home/user/mounts/rclone2/**
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640013902312.PNG)

Navigate to the correct subfolder for that media type (e.g. /home/user/mounts/rclone/media/TV) and once ready, click the **Ok** button at the bottom so new content is added - it should automatically scan the new path.

:::note
Depending on the size of that cloud content, the scan process can take a while to finish!
:::

That was it! Your cloud content is now organized!

:::note 
If you have already installed the app in the past, just click at the **Library import** at the top left section of the screen, the process is the same. Afterwards, you can select that remote mount for your new content that is going to be added.
:::

## Radarr
Once you finish the radarr installation via your client area, visit the app via the link **"Go to application"** (which is essentially https://USERNAME-radarr.cloud.seedboxes.cc/ ) . After logging in with your seedbox credentials, click the **Import Existing Movies** button at the viewscreen.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640014214931.PNG)

At the new screen, click the only button available - **Start Import**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640017338908.PNG)

At the new modal, navigate to **/home/user/mounts/rclone/**  and you will find the content there.

:::note
If you own a Vampire or better tier seedbox, you can mount two remote points. The second can be found at **/home/user/mounts/rclone2/**
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640013902312.PNG)

Navigate to the correct subfolder for that media type (e.g. /home/user/mounts/rclone/media/Movies) and once ready, click the **Ok** button at the bottom so new content is added - it should automatically scan the new path.

:::note
Depending on the size of that cloud content, the scan process can take a while to finish!
:::

That was it! Your cloud content is now organized!

:::note
If you have already installed the app in the past, just click at the **Library import** at the top left section of the screen, the process is the same. Afterwards, you can select that remote mount for your new content that is going to be added.
:::