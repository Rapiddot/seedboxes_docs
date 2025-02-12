# How to use deluge thin client to connect to your deluge daemon from your pc

## Introduction

Deluge torrent client gives you the option to install it locally to your PC and use it as a **thin client** instead of a standalone app. This essentially means controlling your seedbox deluge client from your PC client while downloading your torrents at your seedbox. Of course, in order for this to work, you need to be already using deluge as your seedbox torrent client.

## Installation
Just go to the official [deluge](https://dev.deluge-torrent.org/wiki/Download) page, download the latest version and install it as usual.
**Note**: You should download and install the same Deluge version as the one you have at your seedbox. For the screenshots below, it is shown for deluge v1 but it is generally recommended to use the v2.

## Set up deluge

### Seedbox deluge
As noted, you should already be using deluge at your seedbox. Open up a browser and head to your seedbox deluge client. When the Connection Manager pops up, you should write down your port (five digit number e.g. **52506**, yours should vary from the screenshot), which is right next to the 127.0.0.1 IP address under "Host"

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1604929820983.jpg)
** Note** : If you are already logged in, click the **Connection Manager** tab in order for the window to appear

### Local deluge (thin client)
Then, you need to do the following steps at your **local deluge client** so you can successfully connect to your remote deluge client:
1) Head to **Edit -> Preferences -> Interface** , untick classic mode so it is **disabled**. Hit the apply button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1604929419176.png)

2) Restart deluge. You should now see the Connection Manager pop up

3) Remove the localhost daemon, if there is one

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1604929600908.png)

4) Click the **Add** button. At the new pop-up, for **Hostname** you should enter : **USERNAME-deluge.cloud.seedboxes.cc** . For **Port**, just input the five-digit port number you previously wrote down from your seedbox deluge. For **Username** and **Password**, use your seedbox credentials. Of course, substitute **UPPERCASE** username with your **case sensitive** username.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1686894071300.38.31.jpg)

5) Click the **Add** button. A green tick/circle should now appear as the status for your seedbox host you just added. Select the host, and hit the **Connect** button at the bottom right corner. The connection manager popup should disappear and you will be connected to the deluge client of your seedbox

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1604931010995.png)

And that's it, you can now control your seedbox deluge client from your PC