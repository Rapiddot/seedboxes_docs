---
id: how-to-restart-your-seedbox
title: How to Restart Your Seedbox
description: Learn how to restart your seedbox and troubleshoot common issues such as disk space limits and file deletions.
keywords:
    - seedbox
    - restart seedbox
    - troubleshoot seedbox
    - rtorrent
    - seedbox client area
---

# How to restart your seedbox

All our servers come with automation software, which checks every 30 minutes every aspect of the server to guarantee its normal operation. This service checks if your rtorrent client is running too. If it's not, then it starts it automatically.

There are cases though, that even after the restart, your client continues to be offline. This means that your client has crashed during its startup. Common reasons for rtorrent to crash are:

* Your diskspace limit has been reached
* You tried to delete very large files from within rutorrent.

In this case, you should correct the problem (free some disk space, or delete the files manually via ftp or ssh) and then issue a restart on your client.

In order to do this, follow this simple procedure:

* Login to your client area.
* After you log in to your seedbox account, click in the "My Client Area" button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590755315120.png)

* In your Seedboxes area, click on the little "gear icon" next to the seedbox you want to restart and click on "Restart Seedbox".

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590755346997.png)