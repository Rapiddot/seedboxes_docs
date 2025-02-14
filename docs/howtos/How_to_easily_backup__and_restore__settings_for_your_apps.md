---
id: how-to-backup-restore-settings
title: How to easily backup and restore settings for your apps
description: Learn how to easily backup and restore settings for your apps on your seedbox using Sonarr as an example. This guide covers both backup and restore processes.
keywords:
    - backup
    - restore
    - seedbox
    - Sonarr
    - app settings
    - configuration
---

# How to easily backup and restore settings for your apps

## Introduction

Most of our supported apps have a build-in functionality to easily backup configuration settings, databases etc.
They usually create a compressed "zip" file which is either downloadable (e.g. in case of Sonarr/Radarr) or automatically place it at a path inside your seedbox (e.g. Sabnzbd which places the zip file inside the "Completed" folder, if no "Backup" folder is set).  

This is most handy if something were to happen to the seedbox disk (Disclaimer: We use state-of-the-art Enterprise HDD's. Even though disk failures are incredibly rare, they are expected nevertheless).
You would hate to start from scratch, wouldn't you?
If you keep a backup file to your PC, you can easily restore the settings to the seedbox app and continue from that point and on. With that in mind, some apps offer scheduled backups or do so automatically - you just have to download them locally to your PC and keep that backup somewhere safe.

**Note:** Avoid creating backups from e.g. your PC apps or another service and restoring it at your seedbox apps or vice versa, since it will most likely break things due to paths changing, network settings incompatibility etc.
**This guide is meant only for backing up and restoring settings for/to your seedbox apps**.

## Backup

For the backup functionality, we will use **Sonarr** as an example. Open the app and go to **System -> Backup** .
Sonarr is already taking automatic scheduled backups for your configuration files, you can find them at the section to the right.
Else, you can manually perform the backup, just hit the **Backup Now** button.
After it finishes backing your database up (it might take a while based on how large db you have - you might need to refresh the page though), a new entry will be shown just right below the "Backup Now" button.
The "clock" icon means that the backup was done automatically, the "person" icon means manually, as shown at the screenshot

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1701765585310.36.41.jpg)

Click the link and download the zip file to your PC. This is it!


## Restore

For the restore functionality, we will use **Sonarr** as an example. 

Open the app and navigate to  **System -> Backup** and click at the **Restore Backup** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1701767188949.04.42.jpg)

At the new modal, click the **Choose File** button, navigate locally to the folder that the downloaded database exists and select the zip file.
Once the file gets loaded, click the **Restore** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1615461703219.png)

It will automatically restart once finished restoring.

This is it! You have successfully restored your settings and database to the app!

:::note
Don't forget that you need to re-download the series thumbnails. Just click at the **Update all** button in order to do so.
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1615203398628.png)
