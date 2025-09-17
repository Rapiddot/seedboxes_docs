---
id: how-to-use-jackett-with-sonarr
title: How to use Jackett with Sonarr
description: Learn how to integrate Jackett with Sonarr to scrape torrents and manage your media library efficiently. Follow this step-by-step guide for installation and configuration.
keywords:
    - Jackett
    - Sonarr
    - torrent scraping
    - media management
    - indexer
    - installation guide
---

# How to use Jackett with Sonarr

## Introduction

From the official Jackett app github:
> *Jackett works as a proxy server: it translates queries from apps (Sonarr, Radarr, SickRage, CouchPotato, Mylar, Lidarr, DuckieTV, qBittorrent, Nefarious etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps.*

In this guide, we will be using Jackett for scraping torrents into Sonarr app

## Installation
Go to your client area, click the **Installable Apps** section and add both applications via **+Add Application** button. You can find a more detailed guide regarding 1-click installation of the apps [here](./How_to_install_our_1-Click_applications.md)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558953823325.png)

### **Jackett**
Click **Go to Application** and a new window will be opened. After your successful login, then main page of the Jackett app will appear. On the top right corner you can find your **API Key** that will be needed afterwards

1) Click **+Add indexer** to add your indexer of your choice

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558516825927.png)

:::note
The API Key credential shown at the screenshot is temporary and used only for this guide. Your key will -obviously- differ than the one shown here.
:::

2) Let's say we want to use *Torrentz2* . Scroll downwards and click the **wrench** icon at the right section.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559199850160.png)

This will open up the settings of that indexer. Write somewhere down the **codes** for the categories you are interested in as Sonarr needs manual input of the codes (e.g. 2040 for Movies/HD, 5000 for TV etc). Alternatively, you can click the wrench icon of the indexer once you add it, so you can see at a later state the codes you will be needing.
Press **Okay** button afterwards to add the indexer.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559200290148.png)

Your will be automatically navigated to Jackett's main screen where you can see that the indexer was successfully added.

:::note
Don't close the window yet, as it will be needed later for the **API Key** and **URL** field at the **Sickchill** app.
:::

### **Sonarr**

Assuming you have being already using the Sonarr app, this guide will only show how to add and use the custom indexer.

At the main page of Sonarr, click **Settings** icon and you will be redirected to the first tab (Media management)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558953988637.png)

#### **- Indexers**

1) Click **Indexers** tab to set your custom indexer, where in this case you will be using a custom Jackett indexer.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558954766755.png)

2)  Click the **Custom** button at **Torznab** section, under *Torrent*

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558954821301.png)

At the new modal, choose a name of your choice (e.g. *Jackett (Torrentz2)*). Now for the rest two fields, you need to head back to your Jackett app.

Click the **Copy Torznab Feed** button in order to copy the link and paste it at the **URL** back at the Sonarr app.
Similarly, copy from the top right corner the **API Key** and paste it at the corresponding field back at the Sonarr app

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559202493052.png)

At the **Categories** field, input the codes you have noted in the previous steps (or just click the **wrench** icon at the configured indexer back at your Jackett app) for your indexer to search in.
After inputting all fields, you can click the **Test** button to check if everything went smoothly and finally click the **Save** button:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1589956658599.png)

You are now ready for adding your favourite shows via your custom indexer!


