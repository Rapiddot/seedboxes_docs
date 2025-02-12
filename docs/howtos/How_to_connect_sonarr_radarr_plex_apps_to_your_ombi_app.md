# How to connect sonarr, radarr and plex to your ombi app

## Introduction

From the official ombi website:
> *Ombi is a self-hosted web application that automatically gives your shared Plex or Emby users the ability to request content by themselves! Ombi can be linked to multiple TV Show and Movie DVR tools to create a seamless end-to-end experience for your users*

In this guide, we will be showing how to connect your sonarr, radarr and plex apps to ombi

## Installation
Go to your client area, click the **Installable Apps** section and add ombi via **+Add Application** button. You can find a more detailed guide regarding 1-click installation of the apps [here](./How_to_install_our_1-Click_applications.md). Of course, you need to already have set up sonarr and radarr apps, as well as plex too.

After ombi installation from your client area, open the link to navigate to your ombi app. You will be asked to to choose your media server. For the time being, we support only **Plex** so choose that.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1603785738718.png)

At the next screen, click at the **Continue with Plex** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1603785880598.png)

A pop-up window will open so you can input your plex credentials and sign-in via plex.
**Note**: If you are already signed in to your plex account, just scroll down and click the **Sign in** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1603786414556.png)

After logging in, you can manually close the pop-up window - if that is not done automatically

### Connect sonarr / radarr

Just head to **Settings** and then at **TV** and choose **Sonarr** from the dropdown menu.

To the left section of the screen, input your credentials as:
Enable: Checked
Host for sonarr: **username**-sonarr.cloud.seedboxes.cc
Port: 443
SSL: Checked
API Key: You get it from the general settings of sonarr app

Of course, substitute username with your seedbox username.

After you input your credentials, go the right section of the screen and click the **Load qualities** and **Load Folders** button.
**Note**: These are already set up and taken by your sonarr app.

Choose your desired quality from the dropdown menu as well as the correct paths, like shown at the screenshot below:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1603788214792.png)

Finally, click the **Test connectivity** button to make sure you have input everything correctly and then click the **Submit** button.

The exact same procedure must be done for Radarr too, just go to **Movies** and choose **Radarr** too.
The only thing that changes is the 'Host: **username**-radarr.cloud.seedboxes.cc' and the api key which again, you get it from the general settings of radarr app


### Connect plex

Navigate to **Media server** and choose **Plex** from the dropdown menu.

At the right section of the screen, input your username and password plex account credentials and click the **Load Servers** button. Your available plex servers will be fetched from your plex account and you can now select the seedbox server from the dropdown menu **Servers** just below.
It should be something like **username**-plex.cloud.seedboxes.cc (if you haven't renamed the server at your plex app) .
After you choose it, you wil see that most fields are populated at the left section of the screen. However, some changes are needed to be done, as following:

Host: **username**-plex.cloud.seedboxes.cc
Port: 32400
SSL: Unchecked

Of course, substitute username with your seedbox username.

Most probably you will be wanting to monitor all of your plex libraries so you don't have to click at the **Load Libraries** button.
Click at the **Test connectivity** button to make sure you have input everything correctly and then click the **Submit** button.

Congratulations! You have connected sonarr, radarr and plex apps to your ombi and now you are ready to search for content