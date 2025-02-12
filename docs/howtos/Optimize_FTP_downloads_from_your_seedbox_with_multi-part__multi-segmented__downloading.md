---
toc_min_heading_level: 2
toc_max_heading_level: 4
---

# Optimize FTP downloads from your seedbox with multi-segmented downloading

## Introduction

When you download a single yet large file via FTP, that file is being downloaded as a "whole" (one-part file). However, sometimes you might be getting low downloading speeds due to a not-so-great peering between your ISP and your seedbox, or due to high latency because of the distance between yourself and the location of your seedbox.

There is a way to maximize that speed, by "breaking" that file into several smaller pieces, thus creating a new FTP connection for each smaller piece. This process is called **multi-part** or **segmented** downloading.
However, there is a caveat; a great number of FTP clients (like the popular Filezilla) don't support that process.
So if you find yourself the need to download at your maximum ISP line capacity, you should use one of the following FTP clients, depending on your operating system.

**Note**: **Multi-part** downloading is not to be confused with **multi-threaded** downloading where you can download simultaneously many different files (something that e.g. Filezilla and many FTP clients support). This guide is about downloading a single file via FTP, as fast as you can.

## Installation
Just a reminder regardless of Operating System, you can find your login credentials at the **Login information** as well as your connection info at **FTP Access**, at your **seedbox control panel** [here](https://www.seedboxes.cc/client/dashboard) and by clicking your corresponding seedbox name

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557384850265.png)

### 1) Windows

You can find several FTP clients that support multi-part downloading such as CuteFTP, iGetter, smartFTP etc. In this guide, we will be using CuteFTP or iGetter.

#### **- CuteFTP**

:::info Note
Older versions of CuteFTP are deprecated (like version 9.0 as shown at the screenshots below) and cause authentication issues. You need to **upgrade** to the latest version available. 
:::

After installing the client, navigate to **File -> New -> FTPS TLS/SSL (AUTH TLS - Explicit)** in order to create the secure FTP connection

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557324209908.jpg)

At the **General** tab, choose whatever name you want for the Label and fill out the rest fields according to your connection info

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557324793914.png)

After that, navigate to **Type** tab, and write the correct port (**9979**) for the FTP connection

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557324868790.png)

You can leave all other fields / tabs with the default settings. Press **Connect** to create and accept the certificate

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557325024264.jpg)

Your connection to your seedbox is now ready. The right panel is used to navigate through your seedbox folders in order to choose the file you want to download locally, and the left panel is used for your PC to navigate through your local folders in order to choose the destination folder.
After navigating at both panels, right click the file and choose **Download Advanced -> Multi-part Download -> MAX (4 parts)**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557384411582.png)

CuteFTP will -temporary and- automatically create the rest 3 parts so there are 4 parts downloading simultaneously in total. When all downloads finish, it will automatically unite all parts into a single file

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557384668183.png)

#### **- iGetter**

After installing the client, go to **Site Explorer** at the left panel, right click it and choose to **Enter Site URL**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557823516260.png)

Enter the URL, your username and password and click **Go**
An example of the URL is:
> ftps://**seedboxuser**.cloud.seedboxes.cc:9979/

Replace the word in bold with your username

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557823690301.png)

Click the FTP Site under the **Site Explorer** , navigate to file path you wish to download, right click the file and select **Add to queue**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557823918469.png)

Go to the "Downloads" section at the top left corner of the left panel and you will now see the file to be ready for downloading. Select it, right click and choose **Item Settings...**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557824865261.png)

Choose number of segments you want the file to break to, and also make sure that the at the FTP connection just below, you have selected **FTP over SSL (explicit) ** 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557824950377.png)

Select the file once more, right click it and choose **Start**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557825241240.png)

:::info Note
You could also use **lftp** command line utility instead of FTP clients that have a GUI, should the need for terminal use arise. Just head to **Linux** section for more information.
Also, **cyberduck** is now available for windows 10 (except OSX), so head to the section below to see more information. The UI has minor changes though, but the general idea is the same - once your download starts, a number at the bottom right corner will appear (default: 9) which shows the number of connections (parts)
:::

### 2) Mac OSX

There are very few FTP clients for OSX that support multi-part downloading, like Cyberduck or iGetter. In this guide, we will be using Cyberduck.

#### **- Cyberduck**
After installing the client, click **Open Connection** at the top left corner and from the drop-down menu, choose **FTP-SSL (Explicit AUTH TLS)** .
Fill out the rest fields according to your connection info

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557392158221.png)

After you get connected, navigate to your remote folder and find the file you want to download. Right click and choose **Download** - it will start downloading the file at your local **Downloads** folder

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557392269472.png)

A new window will appear with your transfers. Click at the **Connections** at the top right corner

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557392412259.png)

At the drop-down menu, choose the number of connections (parts) you wish the file to be divided to

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1557392537784.png)

**Note**: For Windows 10, the UI is a bit different, there is no drop-down menu for choosing the number of connections. However, there is a number at the bottom right corner (default: 9) which states how many connections are selected.

After finishing downloading, Cyberduck will automatically join all parts to the single file

#### **- iGetter**

You can find the guide for the iGetter FTP client at the Windows section

**Note**: You could also use **lftp** command line utility instead of FTP clients that have a GUI, should the need for terminal use arise. Just head to **Linux** section for more information

### 3) Linux

Unfortunately, for linux there is no available client with a GUI (Graphical User Interface) that supports multi-part downloading. Your only option is through command-line, by using either [aria2](https://aria2.github.io/) or [lftp](https://lftp.yar.ru/) .

#### **- aria2**

After you install the utility, open up a terminal, navigate to the local folder you wish to download the file to, and issue the following command;
```bash
aria2c --ftp-user=**user** --ftp-passwd=**password** -s8 -x8 ftp://**user**.cloud.seedboxes.cc:9979/**files/Photo\ Collection.zip**
```

Replace user and password accordingly, update the FTP url too as well as the path of the file and choose how many parts you want the file to be splitted too (*-s8* means split file to 8 connections and *-x8* means 8 maximum connections per server)

:::info
 Aria2 still doesn't support FTPS (encrypted traffic), so if you want the traffic to be encrypted, you should change the protocol to SFTP (and also the port). Even though this guide is for FTP, if you want both encryption and multi-segment, you need to change it to either SFTP, or continue to use FTP while also using our [wireguard VPN service](../Quick_Start/How_to_use_your_Seedboxes.cc_VPN_service).
 :::

For the above example in SFTP, it should be:

```bash
aria2c --ftp-user=**user** --ftp-passwd=**password** -s8 -x8 sftp://**user**.cloud.seedboxes.cc:2222/**files/Photo\ Collection.zip**
```

#### **- lftp**

Contrary to aria2, with lftp you can have a shell once you connect to your FTP, which means that you don't have to remember or know the file's source path. Just open up a terminal, navigate to the local folder you wish to download the file, and issue the command **lftp**
Once you are the lftp's shell, connect to your seedbox by issuing the following;

```
open -u **user**,**password** -p 9979 **user**.cloud.seedboxes.cc
```

Replace the words in bold accordingly to your information. Once you connect, write;
```
pget -n 10 **path/to/file**
```

This will split the file to 10 concurrent segments.

Of course, if you know beforehand the remote path of the file, like in the aria2 example, you can directly download it from your linux terminal by issuing;

```
lftp -u **user**,**password** -p 9979 **user**.cloud.seedboxes.cc -e 'pget -n 10 **path/to/remote/file** -o **/local/path/to/download/the/remote/file/to/**'
```

For example:

```
lftp -u seedboxuser,seedboxpassword -p 9979 seedboxuser.cloud.seedboxes.cc -e 'pget -n 10 /files/Photo\ Collection.zip -o /home/user/Photos/' 
```

:::note
The single quotes after the **-e** argument and at the very end of the command are both needed!
:::

You can omit the last argument (-o) if you have already navigated to the local folder you wish the files to be downloaded to. Again, replace the words in bold accordingly to your information .

:::note
If you want the traffic to be encrypted, you should create an lftp configuration file prior to issuing the above lftp commands. Make sure though that lftp is compiled with either GNU, TLS or OpenSSL library. Then, proceed to creating the file (copy the whole text and paste it once);
:::

```
echo "set ftp:ssl-auth TLS
set ftp:ssl-allow true
set ftp:ssl-force true
set ftp:ssl-protect-data yes
set ssl:verify-certificate no" >> ~/.lftprc
```

You should be ready to continue with the above commands.

Alternatively, at a one-liner command:
```
lftp -c "set ftp:ssl-auth TLS; set ftp:ssl-allow true; set ftp:ssl-force true; set ftp:ssl-protect-data yes; set ssl:verify-certificate no; open -u **user**,**password** -p 9979 ftp://**user**.cloud.seedboxes.cc -e 'pget -n 10 **path/to/remote/file** -o **/local/path/to/download/the/remote/file/to/**'"
```

Note that at the end of the command, there is a single quote **'** followed by a double quote **"** . Both are needed!