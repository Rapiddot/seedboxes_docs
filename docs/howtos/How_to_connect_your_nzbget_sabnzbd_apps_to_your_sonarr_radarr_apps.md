# How to connect your nzbget or sabnzbd apps to your sonarr or radarr apps

## Introduction

The most common option for sonarr / radarr apps is to set a torrent indexer for searching and adding torrents, either via choosing one of the preset indexers or creating a custom one via [jackett](./How_to_use_Jackett_with_Sonarr.md) . As for the download client, it is already pre-configured with your seedbox's torrent client which works out-of-the-box.

However, there is another way to search and download content without the use of torrents and this done via a usenet  / newsgroup account.

:::note
 If you have already set your usenet indexers and just want to know what credentials to use for sabnzbd / nzbget as a download client to your sonarr / radarr app, just head to the [bottom section](#set-the-usenet-download-client-at-sonarr--radarr)
 :::

## Usenet

In this guide, we will be setting two things. The first one is the indexer via a usenet subscription and the second one is the usenet download client. If you want to exclusively download via usenet (instead of torrents), you have to disable both your torrent indexer(s) as well as your torrent client as the download client. In other words, the same **type** of indexer and download client go hand in hand

### Set a usenet indexer

You need a paid newsgroup subscription in order to be able to search and add content via usenet. There are two options on how to setting up the indexer, either directly at sonarr / radarr app, or using an external app as a single indexer source like **nzbhydra 2** which has some advantages if you have multiple usenet accounts. You could of course set all of your indexers directly at sonarr / radarr. Your choice!

#### - Setting a usenet indexer directly at sonarr / radarr

Head to your sonarr /radarr app and go to **Settings -> Indexers** . Toggle off the **Enable RSS Sync** and **Enable Search** for any torrent indexers you might have already set up (so you can search and add only via usenet), and click the plus sign.

At the **Newsnab** box, click the **Presets** and choose your usenet indexer. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602668127906.png)

At the next screen, you need to input your settings (URL, API key, Categories and Anime categories) exactly as shown at your usenet client area. Make sure that **Enable RSS Sync** and **Enable Search** are enabled, test the connection and save.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602668537117.png)

**Note**: If your indexer is not listed, you need to click at the **Custom** tab instead

#### - Setting usenet indexers via nzbhydra 2

If you have multiple usenet subscriptions, the best way is to install **nzbhydra 2** app from your [client area](https://community.seedboxes.cc/articles/how-to-install-our-1-click-applications) and use it as a single indexer source. From their github:

> *NZBHydra 2 is a meta search for NZB indexers. It provides easy access to a number of raw and newznab based indexers. You can search all your indexers from one place and use it as an indexer source for tools like Sonarr, Radarr or CouchPotato.*

Once in NZBHydra 2 app, choose your indexers according to your usenet account (most common indexers can be found at the presets or else you can set a custom one) and make sure that you have input your credentials and settings correctly. You can find them at your usenet client area.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602665872165.png)

Once finished with setting up the usenet indexers, go to **Config -> Main -> Security** and copy your API key. This will be needed later on by sonarr / radarr

Afterwards, head to your sonarr / radarr app and go to **Settings -> Indexers** . Toggle off the **Enable RSS Sync** and **Enable Search** for any torrent indexers you might have already set up (so you can download only via usenet), and click the plus sign.

Since we set up our usenet indexers via nzbhydra 2, this is a "custom" indexer.
At the **Newsnab** box, click at the **Custom** tab . 

At the new modal, input your credentials as following:

```
Name: Whatever you want
URL: **MYUSERNAME**-nzbhydra.cloud.seedboxes.cc
API Key: 443
Use SSL: Yes 
```

Category and Anime Categories: Check your nzbhydra app at **Settings -> Config -> Categories**

Substitute of course **MYUSERNAME** with your seedbox username, in lowercase.

Also, make sure that **Enable RSS Sync** and **Enable Search** are enabled, test the connection and save.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602681682595.png)

### Set the usenet download client at sonarr / radarr

Once finished up with setting the usenet indexer, go to  **Settings -> Download client** . Disable your torrent client (you already disabled the torrent indexer and again, this is only if you want to download via usenet) and click the plus sign. Choose either the **NZBGet** or the **SABnzbd** app, depending on what you are using. Of course, you must have **already installed** that app from your client area and **set your newsgroup server(s)**, in order to use it as a download client.

At the new modal, input your credentials as following:

```
For *Sabnzbd* :
Host: **MYUSERNAME**-sabnzbd.cloud.seedboxes.cc
Port: 443
API Key: You can get it from the General Settings of Sabnzbd
Category: **tv** (for sonarr - you should create it in Sabnzbd before configuring sonarr) and **movies** (for radarr - same)
Use SSL: Yes
```

Substitute of course **MYUSERNAME** with your seedbox username, in lowercase.

Test the client and save.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602680749168.png)

```
For *NZBGet* :
Host: **MYUSERNAME**-nzbget.cloud.seedboxes.cc
Port: 443
Username & Password of your NZBGet
Use SSL: Yes
Category: **Series** (for sonarr - should already exist in NZBGet) and **Movies** (for radarr - same)
```

Substitute of course **MYUSERNAME** with your seedbox username, in lowercase.

Test the client and save.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1602680813429.png)


You are now ready to use sonarr / radarr apps as usual!
