---
id: how-to-start-using-your-seedbox
title: How to start using your seedbox
description: A comprehensive guide on how to start using your seedbox, manage your client area, and configure your settings.
keywords: [seedbox, client area, settings, torrent client, VPN, FTP, SFTP, SSH]
sidebar_position: 1
---

# How to start using your seedbox

## Introduction
Your seedbox is a small part of a larger, remote server, which we call a slot. You can access your seedbox in various ways and make it do your bidding even when your computer is powered off. Your seedbox is completely independent of any other computers.

## Your Client Area
The first thing you should try after your seedbox has been activated, is to log in to your [client area](https://seedboxes.cc/client/). This is a **custom** software, made by us, in order for you to easily manage your seedboxes, payments, monitor your usage and have a general overview of your account.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590750644522.png)

After you login to your client, click on the "**My Client Area**" button and you will be redirected to the main page of your dashboard which looks like this:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590750745477.png)

As you can see on the picture above, the main page gives you a good overview of your account. On the top you get the main functionalities of your client area (Dashboard, Invoices, Tickets, Settings), right below that panel you can see your available **credit balance** and usage statistics, in the middle a list of your **seedboxes**, **unpaid invoices**, **support tickets** and important **service announcements** and finally on the right, posts from our **blog** and **twitter**. You can edit your profile by cliking on the top right corner to the arrow next to your email-username and click at "**Edit Profile**" as you can see in the image right below.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590753189196.png)

Under your "**CREDIT BALANCE**" there is an "**+Add more**" button from where you can access the "**+Add Funds**" option which allows you to add funds to your account in order for the system to automatically use and pay any future invoices.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491557252178.jpeg)

:::info Please Note

Added funds only work on future invoices. If you have an unpaid invoice, it is better to directly pay it instead of adding funds to your account in order to pay it. Also, in order for an invoice to be automatically paid by funds, the amount of your funds needs to be higher or equal to the amount of an unpaid invoice.
:::

## Your Settings Area
You can access your **Settings** area from the top panel. There you can find some main information about your profile and the option to [change your seedbox password](../howtos/How_to_change_your_seedbox_password.md) if you like. Also here you can find two more settings for you to enable:

* **Api Access**
* **Two Factor Authentication**

The first one, is only used in specific cases and not applicable for most users. For **security** reasons never have this feature enabled unless you are actually using it. The second one offers you the ability for 2 Factor Authentication via Google Authenticator for extra security. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590753248584.png)

## Managing your seedbox
From the main page of your client area, under the list which says **My Seedboxes**, locate the seedbox you want to manage and click the gear icon. In the drop-down menu that appears click on the **Manage Seedbox** option.

After you do that, you will be redirected to a page that looks like this:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590753641368.png)

On the upper part of the page, you can see usage statistics for your seedbox. This is the easiest and more accurate way to know if you are within the allowed limits of your seedbox.

Below the usage statistics, you will find the **General Info** which contains generic information about your seedbox such as server name, server IP, your currently selected torrent client and other useful information. And of course, on the right of the General Info, a nice **Usage graph** couldn't be missing from your client area. You will also notice the "**Restart Seedbox**" button which does what the name implies, restarts your seedbox.

:::tip
Restarting your seedbox, basically just restarts your torrent client. It does not restart any other apps installed in your seedbox. If you wish to restart an app, you can do so in the "Installable apps" tab explained later in this guide.
:::

Moving further down on the page you will find a box with the following tabs:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590753810192.png)

**Seedbox**

Under the **Seedbox** tab you will find the options listed in the figure below:

* **Login Information**: The username and password of your seedbox. From here you can also [change your seedbox password](../howtos/How_to_change_your_seedbox_password.md) if required.
* **Torrent Client WebUI**: Change your default torrent client. Please note that you can only use one **(1)** torrent client at a time.
* **Seedbucket**: This is an advanced -yet extremely easy to use- file manager for your seedbox with an integrated torrent client (rutorrent v3/v4, deluge v1/v2, transmission and qbittorrent supported). You can check our detailed guide [here](../seedbucket/How_to_use_Seedbucket.md).
* **FTP/SFTP Access**: Here you will find all the information for you to establish an FTP or an SFTP connection with your seedbox. By clicking the **Filezilla Configuration** button you will download an automatically generated configuration file for you in order to import to your [Filezilla FTP client and connect to your seedbox via FTP](../howtos/How_to_connect_via_FTP_to_your_account_using_FileZilla.md).
* **SSH Access**: Provides you the information for an SSH connection with your seedbox. 
* **Promo codes**: If you have any promo codes, enter them at the field and click the corresponding button
* **Cancel Seedbox**: If you ever wish to cancel your seedbox, this is the place to do it :(

:::note
The cancellation button in your client area, will automatically cancel your service **at the end of the current billing cycle**. If you wish to cancel your service immediatelly (in order to receive a refund in the first week of your service), please open a support ticket with this request.
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1687938903006.53.19.jpg)

**VPN**

Under the **VPN** tab you will find the options listed in the figure below:

* **Download Configuration**: Here you can download the wireguard configuration for the [VPN service](./How_to_use_your_Seedboxes.cc_VPN_service.mdx).
* **Delete**: Here you can delete the wireguard configuration in order to free a slot and create a new one.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1687939424449.00.36.jpg)


**Installable Apps**

At this last tab you will find our **1-Click Installable Applications**. With the click of a button, you can install any of the available applications you see on the list to your seedbox.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590754200261.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590754208246.png)

If the application you've just installed has a web interface, in order to access it just click the **Go to application** button next to it. All applications have an **Infobutton** which contains useful information and we strongly recommend reading before you install an application.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590754457865.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1590754464820.png)

We always try to have the latest versions available and we always add new applications to the list. All apps are set to automatically update every week.
Feel free to play around with your client area in order to get more familiar with it.

It's time to move to the next step, to actually using your seedbox. This is just a basic guide on how to start using your seedbox but you can do much more advanced things which are not covered here.

## Torrent Clients Web Interface
All our torrent clients (rTorrent, deluge, qbittorrent & transmission) have a web based interface which means that you can easily control your torrent client from your browser. That means, that you can access your torrent client from any device that is connected to the Internet. Even if you close your browser, your seedbox will continue downloading/seeding your torrents normally since it's a completely independent device as we have already explained.

In summary, in order to download a torrent you need to do the following:

* Go to your favorite torrent site and download the .torrent file you want to your computer or copy its magnet link.
* Open the web interface of your currently installed torrent client. If you do not remember the URL of your torrent client, please refer to the "**Connection Details**" of your seedbox within your client area as also described at the top of this guide.
* Add the .torrent file or the magnet link to your torrent client.
* Done! Your seedbox will now do the rest by simply downloading the torrent files which you can access any time.
Below, we will explain in more detail **step 3** for each of the available torrent clients.

:::info Related Articles

* [Which torrent client should I choose?](../faq/Which_torrent_client_should_i_choose.md)
* [Set your default torrent client](../howtos/Set_your_default_torrent_client.md)
:::

### ruTorrent
[ruTorrent](https://code.google.com/p/rutorrent/) is the web interface for [rTorrent](http://libtorrent.rakshasa.no/). Because of the way that ruTorrent uses to communicate with your rTorrent, it is not able to handle more than 1000-1300 torrent files at the same time. 

In order to add a torrent to your ruTorrent you need to do the following:

1. Go to your ruTorrent web interface.
2. From the upper left side, click **"Add Torrent..."**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820328237.png)

1. After you click it, the "Add Torrent" dialog will pop up. If you want to add a .torrent file, then simply use the **"Torrent File"** option. Assuming that you have saved the .torrent file locally on your computer, you can easily add it by using the **"Browse"** button. After you locate the .torrent file, click **"Add File"** and the torrent will automatically be added to your ruTorrent.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820370000.png)
If you want to add a magnet link instead, then simply use the **"Torrent URL"** option which is exactly below. Just paste the magnet link and click **"Add URL"**.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820407802.png)
After you add the torrent, it will appear in the main list from where you will be able to watch its progress and run actions on it, such as removing it, stopping it etc

### Deluge
Deluge provides its own web interface. Even though the web interface is stable, the deluge daemon itself can not handle a large number of torrents (like rTorrent) and it's mostly used for more aggressive seeding.

In order to add a torrent to your Deluge you need to do the following:

2. Go to your Deluge web interface.

3. A password prompt will appear. Enter your seedbox password and click **"Login"**.

	![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820528584.png)

4. After you successfully login, the **"Connection Manager"** dialog will appear. Inside your connection manager, you should be able to see your Deluge daemon with status **"Online"**. Simply select it and click **"Connect"**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820560625.png)

5. You are now connected to your deluge daemon. You can now easily add a .torrent file or a magnet link by simply clicking **"Add"** on the upper left side of your deluge interface.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820584629.png)

6. The **"Add Torrents"** dialog will popup. If you want to add a .torrent file (which you have previously saved locally on your computer) use the **"File"** button or if you want to add a magnet link, simply click on the **"Url"** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820642518.png)

After you add the torrent, it will appear in the main list from where you will be able to watch its progress and run actions on it, such as removing it, stopping it etc

### Transmission
Transmission, just like Deluge, comes with its own web interface. Even though is very simple and clean, it's not the most popular client. It's mostly used if you have a very low number of torrents and you are not interested for advanced usage.

In order to add a torrent to your Transmission you need to do the following:

7. Go to your Transmission web interface.

8. On the upper left corner, click the **"Open Torrent"** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820694052.png)

9. After you click the Open Torrent button the **"Upload Torrents Files"** dialog will appear. From here, you can either add a .torrent file(s) by clicking on the **"Choose Files"** button or you can add a magnet link in the URL input box below and click **"Upload"**.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491820703127.png)

After you add the torrent, it will appear in the main list from where you will be able to watch its progress and run actions on it, such as removing it, stopping it etc. As you can see, from all three, Transmission is the simplest one.

### Qbittorent
Qbittorent is the torrent client with a lot of features support. 

In order to add a torrent to your Qbittorrent you need to do the following:

10. Go to your Qbittorrent web interface.

11. On the upper left corner, click the **"Plus"** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1687940261809.15.02.jpg)

12. At the new modal, click **"Browse..."** button in order to upload the '.torrent' file (or files as you can upload multiple) and the hit the **"Upload Torrents"** button.
 
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1687940607221.18.38.jpg)

## Connecting to your seedbox
We support a numerous ways and protocols to interact with your seedbox, to download your files to your computer or to use it for anonymity on the internet.

### SSH
In order to interact with your seedbox you can do it via [SSH (Secure Shell)](http://www.wikiwand.com/en/Secure_Shell). This is basically a linux console which allows you to do more advanced things in a more efficient way, such as copying files from a remote server to your seedbox. Since the use of the linux terminal is a complex topic, we will not be covering it in this guide.

**Related articles:**

* [How to connect via SSH to your account](../howtos/How_to_connect_via_SSH_to_your_account.md)

**Recommended SSH clients:**

* [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) (Windows)

### FTP / FTP + SSL / SFTP
The easiest way to download your torrent files to your computer (or anywhere you want) is via [FTP (File Transfer Protocol)](http://www.wikiwand.com/en/File_Transfer_Protocol). We support both unencrypted FTP connections and encrypted FTP connections with the latter one as the strongly recommended way. SFTP (SSH File Transfer Protocol) is also supported but it's slower than FTP + SSL so the latter one is preferable since both have the same encryption strength.

:::info Related Articles
* [How to connect via FTP to your account using FileZilla](../howtos/How_to_connect_via_FTP_to_your_account_using_FileZilla.md)
:::

**Recommended FTP/FTPS/SFTP clients:**

* [FileZilla](https://filezilla-project.org/)(Windows, Linux, MacOSX)
* [Cyberduck](https://cyberduck.io/?l=en) (Windows, MacOSX)
* [WinSCP](http://winscp.net/eng/download.php) (Windows)

### How to use your seedbox for anonymity

We offer a wireguard VPN solution to mask your identity on the internet, that comes for free with your seedbox.

VPN will encrypt **ALL** your network traffic from your computer to the internet and mask your identity. The disadvantage of using this is that since ALL your network traffic is encrypted, it might slow down your connection (though it should be negligible). 

:::note
Depending on the seedbox plan, you can use 2-5 different VPN connections simultaneously. A wireguard connection created in your client area can be installed in many devices if you wish, but only one of them can be connected actively. This is a limitation of the way Wireguard works. If you try to connect at the same time from a second device with that same connection, it will either fail or your previous connected device will log out automatically.
:::

:::info Related Articles
* [How to use your Seedboxes.cc VPN service](./How_to_use_your_Seedboxes.cc_VPN_service.mdx)
:::