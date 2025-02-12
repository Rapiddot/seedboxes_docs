# How to use Jackett with Sickchill

## Introduction

From the official Jackett app github:
> *Jackett works as a proxy server: it translates queries from apps (Sonarr, Radarr, SickRage, CouchPotato, Mylar, Lidarr, DuckieTV, qBittorrent, Nefarious etc) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps.*

In this guide, we will be using Jackett for scraping torrents into Sickchill (Sickrage) app

## Installation
Go to your client area, click the **Installable Apps** section and add both applications via **+Add Application** button. You can find a more detailed guide regarding 1-click installation of the apps [here](https://community.seedboxes.cc/articles/how-to-install-our-1-click-applications)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558516564315.png)

### **Jackett**
Click **Go to Application** and a new window will be opened. After your successful login, then main page of the Jackett app will appear. On the top right corner you can find your **API Key** that will be needed afterwards

1) Click **+Add indexer** to add your indexer of your choice

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558516825927.png)

:::note
The API Key credential shown at the screenshot is temporary and used only for this guide. Your key will -obviously- differ than the one shown here.
:::

2) Let's say we want to use *Torrentz2* . Scroll downwards and click the **wrench** icon at the right section.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559199850160.png)

This will open up the settings of that indexer. You don't have to write down the codes for the **categories**  as Sickchill offers to automatically import them.
Press **Okay** button afterwards to add the indexer.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559200290148.png)

Your will be automatically navigated to Jackett's main screen where you can see that the indexer was successfully added.

:::note
Don't close the window yet, as it will be needed later for the **API Key** and **URL** field at the **Sickchill** app.
:::

### **Sickchill (sickrage)**

Assuming you have being already using the Sickchill app, this guide will only show how to add and use the custom indexer. However, if you are new here, there is an excellent [guide](./How_to_use_Sickchill__Sickrage__with_your_seedbox.md) regarding the installation and proper setting up of the app.

At the main page of Sickchill, hover your mouse on the **gears** icon and choose **Search settings** from the dropdown menu

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558530854171.png)

#### **- Search settings**

1) At the new window, click **NZB Search** tab, and tick the **enable NZB search providers** if you are not already using them. Choose **Black hole** for sending .nzb files to, and **Browse** for the appropriate folder location. You can copy-paste the path from this guide or else browse and navigate to that same folder.

> */home/user/torrents_blackhole*

**Note:** You **HAVE** to choose that particular folder or else your torrents won't be automatically added!

Click **Save changes** button under the *Black hole folder location* and once more, click the similar button at the bottom left corner

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559204826841.png)

#### **- Search providers**

2) Hover your mouse at the **gears** icon at the top right corner, this time choosing **Search Providers** from the dropdown menu

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558530883650.png)

Since you will be using your custom providers via Jackett app, head to the third tab **Configure Custon Newznab Providers**.
Select **--add new provider --** from the dropdown menu, and give it a label of your choice (e.g. *Jackett (Torrentz2)* ). Now for the rest two fields, you need to head back to your Jackett app.

Click the **Copy Torznab Feed** button in order to copy the link and paste it at the **Site URL** back at the Sickchill app.
Similarly, copy from the top right corner the **API Key** and paste it at the corresponding field back at the Sickchill app

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559202493052.png)

After inputting all fields, click the **Add** button:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1589958330007.png)

Select which search categories you want (for faster configuration, you can select all of them) and click the **Update Categories** button . Don't forget to finalize your settings by clicking the **Save Changes** button at the bottom left corner!

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1589958494911.v2.png)

3) Now your custom search provider is set. Click the first tab **Provider Priorities** in order to enable your custom provider

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531027525.png)

4) Your new provider should appear at the bottom of the list. **Tick** to enable it and click **Save changes** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531038222.png)

5) After finishing up with the **Provider Priorities** (first tab), click the **Provider Options** (second tab) at the top left corner of the Search Providers. Configure your provider and enable the search options as in the screenshot. Again, at the end click **Save changes** button at the bottom left corner.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531149293.png)

You are now ready for adding your favourite shows via your custom indexer!