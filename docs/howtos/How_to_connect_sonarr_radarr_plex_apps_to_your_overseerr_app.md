# How to connect sonarr, radarr and plex to your overseer app

## Introduction

From the official overseerr website:
> *Overseerr is a request management and media discovery tool built to work with your existing Plex ecosystem.*

In this guide, we will be showing how to connect your sonarr, radarr and plex apps to overseerr


## Installation
Go to your client area, click the **Installable Apps** section and add overseerr via **+Add Application** button. You can find a more detailed guide regarding 1-click installation of the apps [here](./How_to_install_our_1-Click_applications.md). Of course, you need to already have set up sonarr and radarr apps, as well as plex too.

After overseerr installation from your client area, open the link to navigate to your overseerr app. You will be asked to sign to your plex account

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662456888071.20.42.jpg)

A pop-up window will open so you can input your plex credentials and sign-in via plex.

:::note
If you are already signed in to your plex account, just scroll down and click the **Sign in** button
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662456906863.22.23.jpg)

After logging in, you can manually close the pop-up window - if that is not done automatically

### Connect plex

After login, you will be automatically redirected to connect your plex server to your overseerr app.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662456976969.23.15.jpg)

Just click the refresh blue button at the right section of the screen so it fetches your available servers.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662458169122.23.15.jpg)

To the left of that button, there is a dropdown menu with all of your available plex servers. Just pick the one that resides inside your seedbox (note: if you have multiple seedboxes, you can pick up which ever seedbox plex server you  want), it should be something like:

> USERNAME-plex.cloud.seedboxes.cc

Of course, the word USERNAME will be automatically be replaced with your current seedbox username you picked.
Also, if you see multiple entries, just pick the first ones that don't have digits and have the [remote] and [secure] tags

It will automatically input all necessary fields (host/port/SSL), so it should be something like this;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662458195593.26.42.jpg)

:::note
Make sure that the port is **443**, the "Use SSL" is **enabled**, and the host is **USERNAME-plex.cloud.seedboxes.cc** (and like before, the correct username will be shown there)
:::

Click the **Save Changes** button

Next, just below you will find the **Sync Libraries** button. Just click it and it will fetch all of your plex libraries.
Enable the ones you want to monitor (note: you most probably want to **enable all** of them) and at the end, click the **Continue** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662458434729.27.22.jpg)


### Connect radarr

You will then be automatically redirected to setting up Radarr (and Sonarr).

Just click the **+ Add Radarr Server** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662458530167.27.47.jpg)

At the modal, you have to do the following;
1) Choose if this is a default server or a 4K server. You most probably want the first one
2) At the **Server** name, you can choose whatever name you want. Or just manually input the USERNAME-radarr.cloud.seedboxes.cc
3) At the hostname, you need to input the **USERNAME**-radarr.cloud.seedboxes.cc. Again, substitue the bold word with your seedbox username
4) For port, input **443**
5) **Enable** SSL
6) API Key: You get it from the general settings of radarr app, so just open a new tab, go to radarr settings -> General and click the copy button in order to copy it to clipboard. Then just paste it at your overseer field

At this point, you should have something like this;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662458844782.29.10.jpg)

All other required fields are momentarilly blocked. You need to click the **Test** button in order to connect to your radarr app and fetch profiles, root folders and availability.

Once you do, they will be fetched and just select the defaults you want to use.

Once everything is set up, just click the **Add Server** button at the bottom right section of the modal

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1662459054360.33.09.jpg)


### Connect sonarr

The process of connecting sonarr is almost identical to your radarr app.
The only thing that essentially changes (in comparison to radarr) is the host and API key. For the host, use the following;

> **USERNAME**-sonarr.cloud.seedboxes.cc

Again, substitue the bold word with your seedbox username 

You get the API key from the general settings of sonarr app, so just open a new tab, go to sonarr settings -> General and click the copy button in order to copy it to clipboard. Then just paste it at your overseer field

Congratulations! You have connected sonarr, radarr and plex apps to your overseerr and now you are ready to search for new content