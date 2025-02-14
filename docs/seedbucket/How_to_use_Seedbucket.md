---
title: How to use Seedbucket
id: how-to-use-seedbucket
description: A comprehensive guide on how to use Seedbucket for managing your seedbox, including installation, dashboards, external storage drives, and more.
keywords:
    - Seedbucket
    - seedbox management
    - file manager
    - torrent client
    - external storage drives
    - cloud storage
    - encryption
    - media library
    - download center
    - profile settings
    - dashboards
    - discover movies
    - TV shows
    - rclone
    - resumable uploads
    - file sharing
    - torrent client settings
    - labels
    - speed limits
    - file preview
    - starred folders
    - sync files
    - encryption keys
    - media indexers
    - quality profiles
    - advanced settings
    - file operations
    - compress archives
    - create torrents
    - add torrents
    - share files
    - download files
    - upload files
    - torrent details
    - connection manager
    - edit torrent
    - search torrents
    - torrent client dashboard
    - bottom bar
    - changelog
    - global controls
    - statistics

toc_min_heading_level: 2
toc_max_heading_level: 4
---

# How to use Seedbucket
<div class="center-img">
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1505995608698.png)
</div>

## Introduction

Seedbucket was developed in-house by Seedboxes.cc, in an effort to be an one-stop modern alternative for your day to day seedbox management. It has an integrated state of the art **File Manager** and a **Torrent Client** Web UI. Also, it supports a new **Discover** capability for movies and series, a **Library** for your media content, as well as a **Download Center** for all kinds of downloads.

Our plan is to keep improving seedbucket very often and keep adding features in order to make it as user friendly and useful as possible!

## Installation

Seedbucket comes pre-installed with any type of seedbox tier. To use it, just go to [https://seedbucket.seedboxes.cc/](https://seedbucket.seedboxes.cc/) . Input your email / password and you are ready to use it!

You can also find the link at your client area. Just click the **"Go to Seedbucket"** button and a new window will open with your seedbucket.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1633605937228.png)


## Dashboards

Dashboards are still under heavy development but the idea behind it is that you will be able to setup a custom layout with a combination of individual components. For example, you will be able to create a split layout which on the left side will have a file manager with your seedbox files and on the right side your torrent client. However, this is not fully ready yet at the moment which means you are currently limited to connecting an external storage drive and managing its files.

We currently support **Google Drive**, **Dropbox** , **OneDrive** , **FTP**, **SFTP** and **S3** (as well as their **Crypt** drives).

Your Seedbucket comes pre-installed with five dashboards at the main sidebar (left section of screen); **Discover** which is used to discover movies and series (either existing or upcoming), **Library** to manage your media content in conjunction with Discover, **username** (which will be the username of your seedbox) for managing your seedbox files, **Download Center** to manage your downloads and **Torrent Client** which by default is pre-configured to connect to your seedbox default torrent client. Of course, if you own more than one seedbox, another dashboard will appear with that username for dashboard, above the "Torrent Client" dashboard. The latter will include all torrent clients from all of your seedboxes - you have the option to swap view from one to another, set a default etc. More for that later on..

### Add an external storage drive

The process of adding an external storage drive to your Seedbucket account is very simple. You just select the storage drive type and proceed to authorizing Seedbucket to access your cloud files.

This can be done via two ways; Either going to your **Settings -> Drives** and clicking the **"Add storage drive"** button, or -more preferably- by clicking the **+New** button at the main sidebar (left section of the screen) which will also connect a dashboard for that added drive too.

**NOTE:** If you want to just add a storage drive but without connecting it to your dashboard, that is totally fine! Copies from your seedbox towards storage drives can be done without having them connected to your dashboard. However, it is **better if you connect a dashboard too** as you will have a GUI representation of your storage drive files that will also enable you to copy them between all storages or towards your seedbox, as well as load up torrent files directly towards your torrent client etc.

The combo of adding a storage drive and connecting it to your dashboard is **recommended** and can be done as following;

**1)** Click on **"+New"** on the left main sidebar

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470531678.PNG)

**2)** If this is the first time you do this then you will only see your seedbox username. Click the **Add storage drive** button to continue

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1670566548630.15.14.jpg)


#### **Google Drive**
You will be prompted to choose a storage drive type. For a Google Drive storage, just select the corresponding option;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042541085.54.34.jpg)

You will be re-directed to the Google authorization page where you will need to authorize your Seedbucket in order to be able to access your Google files.  


##### **Google Team drive**

The process is almost the same as with the personal Google drive just above.
Once you authorize the drive, the "Select drive" modal will appear with all team drives that you are currently sharing. Just select the one you want to add and click the **Add** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470601598.PNG)

Afterwards, the dashboard modal will ask you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)

#### **Dropbox**
Adding Dropbox to your file manager is also an option. We support both personal and business (team) accounts

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042559259.54.39.jpg)

The process of allowing Seedbucket to access your Dropbox is similar to those above. Alternatively, if you have enabled a third-app authenticator (e.g. Authy) for your Dropbox account, you need to provide the generated code

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1542797770756.png)

Once you authorize the drive, the dashboard modal will appear asking you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)

#### **OneDrive**
Similarly, if you want to use Onedrive or Onedrive business;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042570460.54.44.jpg)

Depending on your email's Microsoft domain (e.g. @live.com, @outlook.com, @hotmail.com etc), you might be re-directed to the Microsoft authorization page which you will need to authorize Seedbucket in order to be able to access your files

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1542797267701.png)

Once you authorize the drive, the dashboard modal will appear asking you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)

#### **SFTP**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042602261.54.48.jpg)

For an SFTP connection, the form is a bit different

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573818798082.png)

Connecting to your seedbox: 

* **Host:** \{username\}.cloud.seedboxes.cc
* **Port:** You can find your port number under SFTP/SSH access in your client area
* **Home Path:** Like FTP, choose to personalize your home path. e.g. /home/user/files

If you have generated a private key and want to use it:

* **Private Key (Optional):** Copy and paste your private key from the key pair that you generated
* **Passphrase (Optional):** If your key carries a passphrase, paste it here

**NOTE:** The private key MUST be of RSA/ECSDA type with PEM compatibility, which means that is has to be created by issuing the command:
**ssh-keygen -t rsa -m PEM** - it can have whatever length you want, but the default (2048) is more than fine.
Also, don't forget to do **all** of the following:
1. At your seedbox, create the necessary **~/.ssh** folder if it doesn't exist
2. Store the public key (e.g. **new\_id\_rsa.pub**) inside that directory
3. Give the following command to authorize the pair; **`cat new_id_rsa.pub >> ~/.ssh/authorized_keys`**

Choosing file size format

* **Binary**: Choose the filesize shown as 1KB = 1024 bytes
* **Decimal**: Choose the filesize shown as 1KB = 1000 bytes

Once you install the drive, the dashboard modal will appear asking you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)

#### **FTP**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042613284.54.53.jpg)

Before you establish an FTP connection you will have to fill the settings form accordingly;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573818901241.png)

For example, connecting to your seedbox: 

* **Host:** \{username\}.cloud.seedboxes.cc
* **Port:** You can find your port number under FTP Access in your client area
* **Secure (Optional):** To enable TLS, for encrypted transmission
* **Home Path (Optional)**: Personalize your home path. e.g. /files/downloads

Using authentication:

* **Username**: Your FTP username (same as your seedbox username)
* **Password**: Your FTP password (same as your seedbox password)

Choosing file size format

* **Binary**: Choose the filesize shown as 1KB = 1024 bytes
* **Decimal**: Choose the filesize shown as 1KB = 1000 bytes

Once you install the drive, the dashboard modal will appear asking you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)


#### **S3**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042642792.54.59.jpg)

You can add any Amazon S3 cloud provider (e.g. iDrive e2, Minio, Storj etc). Just make sure that you have created at least a **bucket** from that cloud provider web UI as it is necessary to further proceed

At the form, make sure to pick the correct provider from the dropdown menu and fill out all settings - regional is optional - according to that provider's credentials

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042922329.58.45.jpg)

**Note:** Some cloud providers give the **Endpoint** without the **https://** as a prefix, just make sure to add it before pasting the URL

**IMPORTANT:** In case you have enabled the **Server side encryption**  at the provider's web UI, you need to toggle the **Advanced Settings** button and select either **AWS KSM** or **SSE-S3** . Note that this has nothing to do with the Crypt drive (check below), this is referring to if server side encryption is enabled or not

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705043810431.16.39.jpg)

Once you install the drive, the dashboard modal will appear asking you to select the home folder. Just scroll down [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#adding-your-connected-drives-to-your-dashboard)

#### **Crypt drive**
This is a new type of storage and it is referring specifically to encryption via rclone. Before the latest seedbucket version upgrade, encryption was done directly at a cloud's dashboard by choosing either a folder -or the whole drive- for encryption. This however was enabling you to have mixed content (both encrypted and unencrypted at the same time), without being certain if existing content was encrypted or not, especially at whole drive encryption.

We **listened to you** via our survey feedback!

We created this new type of storage drive that is essentially a "layer" above the associated storage drive and it will be able to **a)** encrypt new content that is copied inside it and **b)** show ONLY current encrypted content (as decrypted). Plus, it is easier to manage than before.

You can create crypt drives on **Google Drive**, **Dropbox**, **Onedrive**, **S3** (either with or without server side encryption) and on any **FTP / SFTP** cloud drives, which all those cloud drives will act as "associated" drives to the crypt drives. Therefore, you need to have already added a cloud drive of the above type in order to create a crypt drive.
Else, you will be greeted with the following error;
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1670579936782.57.06.jpg)

Just add at least one cloud storage drive of the above types and you will be able to select that associated drive from the dropdown menu.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470782206.PNG)

For reference, the associated drive won't be able to decrypt the content, so if you navigated via the associated dashboard at an encrypted folder, you would see its name as e.g. "s40h415mrvctc3pbn0jjasnvl0" (like you would see if you navigated at that cloud's web UI) whereas in reality, at the crypt dashboard and based on the encryption settings, it would be shown as e.g. "personal".

**NOTE**: Before adding a crypt drive, please proceed [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#encryption) to find important information regarding the encryption flow for crypt drives, encryption backups and how to complete the process of creating a crypt drive.

Finally, as with the associated drives, once you install the crypt drive, the dashboard modal will appear asking you to select the home folder. Read directly below for what to do from here;

### Adding your connected drives to your dashboard

**3)** After you finish adding your external storage drives, along with any crypt drives (optional), you will be re-directed back to your Seedbucket and specifically at the dashboard modal. The new storage drive will have been added and the dashboard modal will show the connected drives. You will then be able to choose the drive and proceed with creating your new dashboard for that drive when you click **"Next"**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470802863.PNG)

**4)** If you want all the files and folders to be shown when you add the drive, just hit the **Select Drive** without selecting any folder.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470811157.PNG)

Alternatively, if you want only a certain folder (along with any files and subfolders inside that) to be shown, navigate to that folder so you can set it as a home folder and click **"Select Folder"** . Only those files and folders under that home folder will be shown at your dashboard. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470866884.PNG)

**NOTE:** When you add a dashboard with a home folder, you can still copy content outside of that home folder. The dashboard is only for viewing purposes, it doesn't limit the actions you can do to your whole drive.

**NOTE2:** You can have as many dashboards as you want, even for the same added cloud drive. For example, one dashboard can be for your whole cloud drive and one dashboard for the same cloud drive but for a certain folder. One crypt dashboard can be for your encrypted Movies and another crypt dashboard (of the same crypt drive) for your encrypted TV shows. There are no limits!


**5)** Fill in your desired name for your new dashboard, click **"Add"** and you are done!

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470882578.PNG)

**6)** Your new dashboard will appear on the left (main sidebar) and it will automatically open for you the first time you add it

If you need to connect more storage drives, then repeat the above steps! And if you got several email addressess from the same provider, each with its own different cloud storage, you can add them all !

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643470892773.PNG)

## Profile

You can easily access your profile from the upper right corner by clicking on your username and then **"Settings"**. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462258114.PNG)
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462265966.PNG)

### Dashboards Manager

From here you can manage all your connected dashboards. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462281950.PNG)

You can either rename the dashboard by clicking the **pencil** icon, or delete the dashboard by, well, clicking the **Delete** icon.

**NOTE:** By deleting a dashboard, you don't remove the drive too, nor you delete any files or folders. You essentially remove the GUI of that (a.k.a. dashboard). The drive remains in your **"Drives"** manager.
If you want to create a dashboard in the future for an already added storage drive, just click the **+ New** dashboard at the main sidebar (left section of the screen) and select that drive.

### Drives Manager

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462325575.PNG)

From here you can manage all your added storage drives and also check their available disk space (FTP/SFTP excluded).
All available actions appear at the same row with the drive. Please keep in mind that not all drives have the same actions. There are some exceptions, like the **seedbox** drive(s) -easily distinguishable by your username- which comes pre-installed, and can not be deleted.

You will also notice an action for the **seedbox** drive that is not available to the other drives, **Sync** which will force re-index all your files in your seedbox.
For the rest drives, that action is available at the bottom right corner of your screen and it depends on the **path** you have currently navigated to. This means that if you navigate to a nested folder and click at that link, it won't refresh all of the drive but the contents of that folder only.

**FTP / SFTP** drives can be edited if you need to edit some of the information (e.g. change home path or decimal/binary prefixes etc).

Same goes for **S3** drives, you can edit its information - the form is exactly the same as the one that was used for adding it.

For **Crypt drives**, other that the delete icon, you can click at the **Keys** icon. This gives you information regarding the crypt drive, such as the encryption path, the file encryption method, the folder encryption method as well as the password and salt (password2).

**NOTE:** If you click at the **eye** icon, the password/salt will be revealed, but bear in mind that this is the **obfuscated** password and not the original one. This is what rclone uses too at its rclone configuration file, so if you need to transfer the encryption settings to your local rclone conf, just hit the **Copy settings** button. You will obviously need to make some modifications once you paste it, in order to correctly set the mount point name.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462410091.PNG)

**NOTE**: Please proceed [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#encryption) to find important information regarding encryption

**NOTE #2:** By deleting a storage drive from the manager, you remove it completely from your Seedbucket, along with any dashboards, crypt drives that have been associated with that storage drive, starred folders etc. Your files will of course remain **intact**.

Lastly, in case you need to add that storage drive again in the future (or to add a new storage drive in general), you need to click the **+ Add storage drive** button and follow the same procedure of adding the storage and authorizing for using it, like it was described previously [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#dashboards) . Just bear in mind that adding the storage drive this way, it won't show you the dashboard modal after the authorization, so you will be needing to click the **+New** button at the dashboards at the left section of the screen.

### Apps

From this tab, you can install an rclone mount point (or two if you have **Vampire or better** tier seedbox) for your **Google**, **Dropbox** or **S3** drive (**crypt drives** included) that will be available to all other apps.
For a thorough guide regarding all the steps necessary for the installation of the rclone mount point, please check our guide [here](https://community.seedboxes.cc/articles/how-to-mount-a-remote-drive-to-your-seedbox) .

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462439647.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462447543.PNG)

### Preferences

From here you can choose some default preferences that will be used globally. More preferences will be added in the near future.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462469079.PNG)

#### UI Preferences
1) **Default Theme:**
Select your default site theme Select how the site will appear, either with a light or a dark theme. The light theme is preselected.

2) **Torrent ratio color**
Enable torrent ratio color depending on your ratio percentage

#### Search preferences

**1) Search only the current dashboard**
When this is enabled, then the search is done only for the dashboard that is active, which means that results will be shown in a modal for that particular dashboard instead of global search.
**NOTE:** When searching in the torrent dashboard, a list will appear at the torrent dashboard with the results instead of a modal

**2) Torrent client dashboard only - Show results in list instead of global search**
When this is enabled and the torrent dashboard is active, then the search results are filtered in a list inside the dashboard, instead of showing them in a modal

#### Starred folders
You can also add starred (predefined) folders for quick access in move/copy to actions or delete current starred folders. 
Adding starred folders can also be done when you are browsing your file manager - check info below for a thorough procedure on how creating and using predefined (starred) folders

### Media

This is the section for your media indexers, the preferred quality profiles as well as some more advanced settings 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1718881501773.03.17.jpg)

#### Media Indexers

Media indexers are essentially tools for searching and downloading media.
Just click the **Add media indexer** button and a modal will emerge on your screen so you can select the indexer of your choice

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715172963521.09.16.jpg)

You have the option to either search for all available indexers, or filter them by their privacy (public, semi-private or private indexers). Public indexers don't require a username/password, nor care about ratio but might lack in download speeds (in contrast with private indexers).

**IMPORTANT: If you want to use private indexers, BE WARNED THAT THIS WILL BE RECEIVED AS A HIT-AND-RUN due to the fact that after the torrent finishes downloading, it gets automatically deleted (so no seeding afterwards). Unless you are a VIP at that private indexer (or that indexer doesn't care about your ratio), you should avoid using these kind of indexers as you will be probably BANNED from accesssing and using them in the future**

So the safe bet is to always use a public indexer, that is widely known too. Just be certain to fill out any necessary fields (like Base Url, which is easily selected via a drop-down menu), then click the **Test** button on the bottom left corner to check if everything is fine and lastly click the **Add Indexer** button on the bottom right corner. Be warned that if there is a seed ratio field, this will be IGNORED as stated above.

**Note:** You can add as many indexers as you want. For the time being, indexers are used sequentially (meaning in added order). If the first indexer can't find the data, it automatically moves to the second one etc. It is in our TODO list to easily change the indexer order via dragging them to the top/bottom, just stay tuned for the next seedbucket version coming soon!

#### Quality profiles

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1718881579156.16.09.jpg)

There are already four profiles pre-created for you that should cover any need.
The **HD 720p/1080p** that searches for any 720p/1080p quality (whichever the indexer finds first\*), the **HD 1080p** which searches exclusively for 1080p quality, the equivalent **HD 720p** for your 720p needs and lastly the **Ultra HD** for that extra pleasure in 4K.
The default profile is the **HD 1080p** but you can easily change that by clicking the relevant button (**Set as default**) at the profile you wish to set as default.

Right below each quality profile, you can see the ordering (from left-to-right) of each source quality. For example, the HD 720p by default will search for HDTV, then WEBRip, then WEBDL and lastly for Blueray source. 

Of course you can edit those profiles and rename them to your liking, or drag a row (from their handler which is three lines like the screenshot below) to bring it to the top (priority) so the search ordering changes

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715174713640.23.22.jpg)

You can add as many quality profiles as you like!

#### Advanced settings

Lastly, this is an advanced feature which you shouldn't tinker unless you _really_ know what you are doing.
Clicking this setting will expand the menu in order to see all available settings.
You can basically change the size limit of each quality definition by dragging the bar handlers (or rename them if you want).
You can always **Reset definitions** if you do something wrong, just scroll to the bottom of the page and click the equivalent button. Be warned that this will reset ALL definitions though.

## File Manager

Seedbucket comes with a complete file manager that allows you to easily manage your local and remote files and perform operations on them.

By right clicking on either a file or folder, a menu will appear that will allow you to perform various actions, depending on which dashboard you currently are. For your local files at your seedbox, all actions are available. To name a few;

* Standard file operations (create folder/move/delete/rename)
* Compress/Extract archives (rar, zip, 7z, tar, tar.gz and bzip2)
* Create torrent
* Add torrent
* Show media info
* Share a file with 3rd parties via share link which expires after a configurable period
* Generate screenshots from video files
* Copy or move files and folders between cloud storages and/or within the same storage
* Mark a folder as starred folder for quick and easy access when you move/copy items to it

### Copying files and folders

Your file manager provides you the ability to easily copy files and folders within the same storage drive or between different ones. For example you can copy a file from your seedbox to your Google Drive or from your Google Drive to your Dropbox; You can even copy from a storage drive towards a crypt drive so that content ends up encrypted inside the crypt drive - **any combination is possible**.

In order to copy a file or a folder simply select one, or multiple files/folders you wish to copy, right click and **"Copy To"**.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462654657.PNG)

**1)** Right click on the item(s) you want to copy and click **"Copy To"**. A modal will appear which will allow you to choose the destination storage drive and folder. All your connected storage drives should appear in the dropdown list. As a quick option, if you have already set starred folders, you can directly copy the items to that starred folder.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462740569.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462756964.PNG)

**2)** Select the target drive and folder and click **"Copy"** 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462783361.PNG)

**Note**: Crypt drives have a lock icon, indicating that encryption has been set to that drive. This means that the items that will be copied to that drive will gain encryption, as the button **Copy and encrypt** indicates.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462814100.PNG)

**3)** Your transfer will begin in the background and it's status will be shown at the bottom left corner. Clicking that button will expand the jobs' drawer so you can see in details what is happening at the background

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643462841286.PNG)

You can stop the transfer any time by clicking on the abort option once you expand the jobs' drawer.

Also, in case that the content already exists at the destination, there will be two options for you;
**a) Overwrite:** This will copy all files from the beginning
**b) Skip: ** This will skip the existing files and only copy the missing ones.
Either way, once the process is finished, the status will turn green with the text "Copied"


### Moving files and folders

Moving items has the same principles as with copying items (check section above). You can either move them inside the same storage drive or between different storages.
Select the items and right-click for the modal to appear, then choose the **"Move"** action. 
As an added functionality that is viable only to **"Move"** action, you can now drag'n'drop the items inside another folder (or via breadcrumbs).

Stay tuned for enabling drag'n'dropping between different drives too!

### Compress/Extract archives

You can easily create archives with a compression type and compression quality of your choosing. Simply right click on the file or folder you wish to compress, select the output path, the compression settings and just click **"Create"**. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463102576.PNG)

If you wish to extract an archive, simple right click on it, select **"Extract"**.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463115994.PNG)

**Note:** For rar compressed files, you need to select the file with the **.rar** extension. If you choose e.g. the file with **.r01** extension, you won't be able to extract

### Create torrents

Creating torrents has never been easier! Create a folder inside your default download torrent directory, move the files you wish to add to your .torrent file, right click on the folder and choose **"Create Torrent"**, enter your torrent settings and lastly click the "Create" button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463231650.PNG)

**IMPORTANT:** The folder for which you wish to create a .torrent file for, **should reside inside your default download torrent directory (which it is "~/files/downloads/" )**. This is to ensure that after .torrent creation, the torrent data can be seeded from your torrent client.
After the .torrent file is created, right click it and choose **"Add torrent"** and from the connections, your seedbox username (check section directly below for further information) in which the torrent data reside.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1719820798311.57.35.jpg)

This will load the .torrent file into your torrent client and start seeding it.

Lastly, don't forget to download and send the .torrent file to your trackers you chose at the torrent creation step

### Add torrent

Torrent files with the appropriate **.torrent** extension, can be added in your torrent client in an instant. If you have multiple connections (aka multiple seedboxes) you can choose the torrent client of that seedbox you want by choosing the seedbox username

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463370236.PNG)

The torrent will be added to your torrent list to that connected client.

### Share files

You can easily share files (not folders) by simply selecting a file, right clicking on it and then **"Share Link"**. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463441830.PNG)

A share link will automatically be generated for you which you can either destroy or copy any time in order to provide it to whomever you want to download the file. Please do make sure that you do not post those share links in public forums or chat rooms or else anyone will be able to download the file. There is a max limit set for concurrent downloading of those links

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463564650.PNG)

And if you want to resend the same shared link, you can always come back later anytime but within the time limit you have set for the link's expiration time. Just head to your seedbucket, find the file that you have already shared and either click the "chain" icon which is at the **"SHARED"** column or right click the file and choose **"Share link"**, just like you did when you created the shareable link. The modal will appear and you can now copy again the same link.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463633500.PNG)

**NOTE:** If you want to share a folder, you can create a compressed file of this folder and share that file. The user that will download it must uncompress it afterwards.

### File preview

You can preview your files easily (either at your seedbox or any cloud drive) by either selecting the file, right-clicking it and then clicking at the **"Preview"** option at the context menu or you can do so by selecting the file and hitting the **"Space"** key. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1655289816183.42.42.jpg)

For the time being, **png**, **jpg**, **jpeg**, **gif** and **bmp** formats are supported for images (360 and panoramic photos included!), as well as **txt** and **nfo** for text files.

We will be soon adding support for more file types (audio/video included!).

While in preview mode, you can also download the file by clicking on the **“Download”** button in the upper right corner.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1655296261430.png)

### Resumable uploads

Tired of having to re-upload a file due to a network error? Then try our resumable uploads from within your file manager by simply clicking on the **"Upload"** button on the upper right corner

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1654870626479.55.50.jpg)

Drop the files you wish to upload and in case of a network error, then simply re-upload them and after they are quickly checked, they will continue from where they left off!
Also, at the bottom section of the modal, you can change the destination folder by clicking the **Change folder** link, in case you don't want to transfer it to the existing folder you were prior to clicking the upload button.
Of course if you want to upload to a cloud drive, you need to have navigated to that cloud's dashboard (and folder inside that) prior to clicking the button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1654870644970.15.14.jpg)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1506025249411.png)

**NOTE:** Resume capability currently applies only for your local seedbox files. Cloud drives are not supported although we do plan to support it in the near future.

### Downloads

What about downloads? We have implemented a way to directly download stuff not only towards your seedbox but towards any cloud drive you have connected to your dashboard. Various types of downloads are supported and more specifically **torrent** files, **magnet** URI's, as well as any **HTTP / HTTPS** , **FTP** and **SFTP** links.
From within your file manager, you can either navigate towards the path you wish to download, click the **New** button on the top right corner of your screen and choose the **Download** option from the drop-down menu.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1654870664630.55.50_2.jpg)

The download modal will open. At the top section of the modal, you can either **a)** click inside it so the file manager opens in order to select which torrents you want to download or **b)** just drag'n'drop the torrents so they will be automatically selected.

At the bottom section of the modal, you can also paste a magnet link at the bottom section of the modal or paste an http / https / ftp / or sftp link.
You can also change the destination folder by clicking the **Change folder** link, in case you don't want to transfer it to the existing folder you were prior to clicking the download button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1654870938305.22.03.jpg)

**IMPORTANT INFO:**
For torrents or magnets, bear in mind that this is only for downloading them. They will **NOT** be seeded after they get completed and will be removed automatically as soon as they are done. So this is only for the cases that you only want to download something fast, without caring about the ratio or seeding time.
Also, another important piece of information is that the torrent data will be **temporarily** downloaded to your seedbox (even if you chose to download it to a cloud drive) which means you need to have enough available space to your seedbox. If you have multiple seedboxes, the one with the most available disk space will be automatically selected for temporarily downloading

Once you add a download, you can navigate to your **Download Center** dashboard in order to manage (or even add) your downloads. You can find relevant information about the download center [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#download-center)


### Starred folders

Wouldn't you wish there was a quick way to choose folders that you frequently move/copy to, without having to navigate inside them again and again? You can now set predefined folders of your choice, either at your local or cloud-based storage, and even uniquely name them however you want! This will not rename the original folder, it's just an easy reference name used by you.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464219523.PNG)

This way, the copy/move actions are being simplified and faster - no need to open modals, choose storage drives, choose paths etc..

There are several ways to create predefined folders; 

**1)** Just right-click selected folder and choose **"Star folder"** 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464007294.PNG)

**2)** You can hover the mouse pointer at the folder and click the outlied **"star"** icon to the right of the folder's name. The star gets filled and that folder instantly becomes a starred folder! Nice 'n' easy, especially if you don't care about giving it a reference name

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464028626.PNG)

**3)** Similarly, you can click the outlied star icon at the **breadcrumbs** section

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464069272.PNG)

**4)** Finally, you can also add starred folders from the **Preference settings** of your profile

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464083225.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643463996915.PNG)

Bear in mind, the names you give at your predefined folders must be unique - you can't have the same reference name for different starred folders. If you proceed giving the same reference name, there will be a modal at the top right corner informing you that an arithmetic prefix was added next to it so you distinguish it from your already referenced folder.

You can delete the reference name from a starred folder, just pick any option from above and reverse your actions. This will NOT delete the folder, just the reference name of it. 

### Sync files

At the bottom right section of the screen, you will see a **"Sync files"** link. This is used mostly for cloud drives
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464361308.PNG)

Once clicked, it fetches the latest contents **for the folder** you are currently in.
If you need to fetch the latest contents at another folder, you need to navigate to that folder and perform this action again.

Use cases:
Shared cloud drive that many users transfer content via the cloud's drive web ui, offload script that transfers content from your local seedbox Plex subfolders towards your Googe Plex subfolders etc.
In general, if there is an external interaction (meaning outside of Seedbucket) and the contents are still cached, then you should click the Sync files link to make sure that you get the latest at that particular folder.

**Note:** For mobiles, the "Sync files" link can be found at the dropdown menu of **"New"**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464478593.PNG)

### Encryption

**NOTE:** The old way of encrypting folders (e.g. via right clicking the folder) is obsolete.

We have implemented rclone utility for encrypting folders -or even your whole drive, both via the crypt drives! Currently, encryption works on **Google Drive**, **Dropbox**, **Onedrive**, **S3** and on any **FTP / SFTP** drive, so you need to have added those drives first, that will act as the "associated drives" in order for a crypt drive to be created. The crypt drive is essentially a "layer" above the associated drives that will contain only encrypted files/foders.

Encrypting a folder (or a whole drive) means that **new content** that will be copied or moved to that folder will also be encrypted. However, current files and folders, prior to the folder/whole drive encryption, will remain unencrypted and won't be shown inside the crypt drive. Don't worry, your files still exist, as you can see them if you navigate via the associated one.

The recommended way is to create a crypt drive and connect it to your dashboard for having a GUI of your encrypted files and folders. To do that, click the **+ New** button at your dashboard (left section of the screen), click the **Add storage drive** at the new modal, click the **Crypt Drive** option and select the storage drive that will be associated to, from the dropdown menu.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464577668.PNG)

#### New encryption

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464592721.PNG)

Make sure that the first option is selected ( **New encryption** ).

If you don't choose an encryption path, then the crypt drive that will be created will have **whole drive encryption**.
If you select a folder, then the crypt drive will be created for that particular **folder**.

So for whole drive encryption, you just hit the next button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464592721.PNG)

Whereas for specific folder encryption, you navigate to that path and then you hit the next button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464724899.PNG)

For either choice, the next step is for the **Encryption settings** ;
The easiest and fastest way to set up the encryption is using the recommended settings. Both files and folder names that will be copied inside your crypt drive will also be encrypted.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464746033.PNG)

However, it is up to you to choose what encryption method you want for files and folders - we offer full customization. You can either choose to **Encrypt file names**, to **Obfuscate file names** (which is a somewhat simpler encryption method) or **Don't encrypt file names** which just adds a **".bin"** extension to your files.
Furthermore, you can select whether you want to encrypt the **folder names** as well. Both options are straightforward, you either choose to **Encrypt folder names** or **Don't encrypt folder names**. Feel free to visit the official [rclone site](https://rclone.org/crypt/) for a more in-depth analysis regarding the different encryption methods.

The encryption keys include both your password and salt (password2). Salt (password2) is optional but recommended. At this stage, both passwords as referred as **Original** passwords.
Once ready, hit the next button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464762519.PNG)

**NOTE: MAKE SURE YOU WRITE BOTH PASSWORDS IN A SAFE PLACE, PREFERABLY AT A PIECE OF PAPER TOO. IF YOU LOSE THEM, YOU WON'T BE ABLE TO SEE YOUR ENCRYPTED CONTENT IN THE FUTURE**

Now the modal changes to **Encryption overview** so you can see everything you have done so far - the selected encryption path, the encryption methods as well as the passwords.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464792653.PNG)

If you need to edit the settings, just hit the corresponding **Edit settings** button. It will take you to the first step again, but this time all fields will be already selected, so you can make any changes easier and not having to do them all over again.
If everything checks out, click the **Set encryption** button so that the crypt drive can be created.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464828613.PNG)

Now, the dashboard modal will appear which you should be already familiar. Just select a name for your dashboard and click the **Add dashboard** button. A new dashboard will have been created with your crypt drive.

#### Existing encryption

If your files have been already encrypted in the past, you need to select the second option from the dropdown menu.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464849388.PNG)

If you don't choose an encryption path, then the crypt drive that will be created will have **whole drive encryption**.
If you select a folder (or a subfolder inside it), then the crypt drive will be created for that particular **folder**.

So for whole drive encryption, you just hit the next button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464849388.PNG)

Whereas for specific folder encryption, you navigate to that path and then you hit the next button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464876749.PNG)

For either choice, the next step is **Encryption settings** ;
Make sure to use the correct encryption settings as those you have selected when you did the encryption in the past. If you choose the wrong ones, even if you paste the correct passwords in the next step, the encryption won't work and you won't be able to decrypt your current encrypted content.
Once you verify that you selected the correct encryption methods, hit the **Next** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464897112.PNG)

Contrary to the previous step, for the **Encryption keys** you are now required to use the **Obfuscated** passwords (instead of the original ones). You can find the obfuscated passwords at your rclone configuration. Just copy and paste them exactly as you see them.

**Note:** The obfuscated keys are at least 16 characters long and don't have a "meaning" as words, contrary to the original passwords which might be real words.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464941843.PNG)

Now the modal changes to **Encryption overview** so you can see everything you have done so far - the selected encryption path, the encryption methods as well as the **obfuscated** passwords.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464950128.PNG)

If you need to edit the settings, just hit the corresponding **Edit settings** button. It will take you to the first step again, but this time all fields will be already selected, so you can make any changes easier and not having to do them all over again.
If everything checks out, click the **Set encryption** button so that the crypt drive can be created.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464958778.PNG)

Now, the dashboard modal will appear which you should be already familiar. Just select a name for your dashboard and click the **Add dashboard** button. A new dashboard will have been created with your crypt drive.

#### **Important! Save your encryptions keys!**

**WRITE DOWN AND KEEP SAFE BOTH ORIGINAL (NON-OBFUSCATED) AND OBFUSCATED PASSWORDS (KEY/SALT), ALONG WITH THE ENCRYPTION METHODS, BECAUSE IF YOU LOSE THEM, YOU WILL BE UNABLE IN THE FUTURE TO ACCESS YOUR ENCRYPTED DATA !!**

The **original** (non-obfuscated) keys are only shown during the creation of the crypt drive for **new encryptions** and before you finalizing creating them. If you complete the process, there is no way you can find what those keys were. So you must be very cautious if you choose to randomly generate the passwords.

The **obfuscated** keys can be found **after the creation of the crypt drive (or if you choose to create the drive with "existing encryption")**. 
Just head to your **Settings -> Drives** and click the **Key** icon at your crypt drive. The **Encryption overview** modal will open that will contain all necessary information.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643464849388.PNG)

## Discover

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716209944902.58.56.jpg)

Everytime you log in to seedbucket, you will be automatically navigated to this dashboard in order to explore and discover movies and TV shows that you might like, read information about them, watch trailers and more, similar to how IMDB works, but without leaving the app!
You can of course search for content inside the bar that resides at the top middle section of your screen.

If you click inside a title, you will see many details regarding that movie/series, like who is the director/producer, who are the cast, as well as recommendations or similar titles

At the right section of the screen, there is a button **Watch Trailer**, which as the phrase states, opens an in-browser youtube video with the trailer of that title.

There is also an **Add to Library** button which you can easily add the title to your media library. For more details, check below the relevant [section](https://community.seedboxes.cc/articles/how-to-use-seedbucket#library)

## Download center

This is an interface to manage all of your download requests except those that reside specifically inside your torrent client. You want to download something directly to a cloud drive? No problem, just navigate to the **Download Center** dashboard and click the **Plus** icon to the top right corner of your screen.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715245880378.52.41.jpg)

This will open the download modal. Here you can either drag 'n' drop .torrent files inside the main area, or click to open up your PC browser and manually select those files.
You can also enter a **magnet uri** or **http / https / ftp / sftp** link (for which this will also be downloaded simultaneously along with any .torrent files).
Lastly, click the **Change folder** in order to select which storage drive and path you wish the selected items (and/or link) to be downloaded to.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715245925640.52.48.jpg) 

**Note**: You can also navigate to a folder you wish to download something (without opening the download center), clicking the **New** button at the top right corner of the screen and then the **Download** from the drop-down menu, as it has already being said in another section of this guide.
This will open the same download modal, with the exception that now the destination folder is already pre-selected.

**IMPORTANT: You can't seed from the download center**. Once you add a torrent/magnet and it gets completed, the .torrent file gets automatically deleted (so no seeding afterwards). **BE WARNED THAT THIS WILL BE RECEIVED AS A HIT-AND-RUN** if you add torrents from private sources, resulting in BANS from accesssing and using them in the future.
If you want to seed, you must download the torrent file at your **Torrent client dashboard** instead. Just scroll a bit down to the next section for more information on that dashboard.

Once the download request is added, it will be shown at your download center. Also, there will be a "bubble" with a number inside the **Download Center** dashboard, indicating the corresponding active number of downloads.
If you right-click at the selected item, a few options will be revealed. In case something went wrong, you can click  the **Retry** button. If you decided that you don't want to download the file after all, just click the **Abort** button. If you wish to remove the download from the list (**NOTE**: Only the request will be removed, not the data), just click the **Remove** button.
Moreover, if you wish to see some details regarding the download request, click the **Download Details**. 
This will open the bottom bar with all necessary details regarding that download.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715246756459.25.37.jpg)

Bonus tip: You can also double-click at a download request, as a shortcut to opening its download details.

Lastly, any download requests from the **Discover** dashboard will be shown here

## Library

You are given the option to create movie/tv libraries to your seedbox (or any cloud drive) and items via the Discover dashboard. Just click the **Add a Library** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715252165683.26.16.jpg)

At the modal, you give a **name** to your library, choose the corresponding **library type** and finally choose the **Save path** . You can have multiple save paths, as well as multiple libraries for the same type!
The save paths can be anywhere you want. HOWEVER, if you choose a cloud drive, your media player that streams from your rclone mount (that cloud drive) won't be able to pick up new content unless you either restart the rclone mount or scan for library files. Both of these cause a lot of API calls which you should really avoid doing so.

It is -therefore- easier and faster to just choose a save path inside your seedbox and use that same path for your media player libraries, as your seedbox is able to pick new content almost instantly

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715252183554.26.25.jpg)

**NOTE**: Don't forget to [set up your indexers](https://community.seedboxes.cc/articles/how-to-use-seedbucket#media-indexers) too at settings -> media -> media indexers

## Torrent Client

A common user interface for your rTorrent, Deluge, Transmission and Qbittorrent connections is also integrated in Seedbucket. From here you will be able to control any local or remote torrent clients you might have, for all of your seedboxes. At the moment the Seedbucket torrent client is basic but new features are being added every day.

**Please note that some menu options might not exist in all rTorrent, Deluge, Transmission and Qbittorrent connections and in some cases an action menu might not exist at all (e.g. in Torrent Files tab for Deluge) or some features might differ (e.g. Qbittorrent supports multiple labels).**

If you right click on a torrent (after a connection is established and your list loads) you will see the following action menu:

rtorrent:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468653849.PNG)

deluge:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468659737.PNG)

qbittorent:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1683614676743.jpg)

* **Start:** Will start the selected torrent(s)
* **Stop:** Will stop the selected torrent(s)
* **Remove:** Will remove the selected torrent(s), with the option to remove their data from disk as well
* **Force Recheck:** Will force recheck the selected torrent(s)
* **Update Trackers:** Will force announce to the associated trackers for the selected torrent(s)
* **Change Path...:** Will move the selected torrent(s) to the newly selected directory. If your torrent(s) was already seeding then it will be resumed after the move completes
* **Edit Torrent:** Will bring up the Edit Torrent modal in order to edit the torrent trackers, comment and private flag
* **Get torrent file:** If the torrent client connection is your local seedbox connection it will download the torrent file (rutorrent only)
* **Priority:** Will change the priority for the selected torrent(s) 
* **Add Label:** Add or select a new label for the selected torrent(s). Qbittorent supports multiple labels per torrent
* **Category:** Qbittorent only: Add a category based on those you have created at torrent client settings or at qbittorent web UI 
* **Speed Limit:** Deluge only: Adjust torrent's speed limit by slider or input
* **Go To Files:** Will take you to the folder where the torrent files are
* **Torrent Details:**: Will bring up the torrent details drawer

### Connection Manager

Once inside the torrent client dashboard, you can see from the dropdown menu the connected torrent clients. If you have multiple seedboxes, then all of your torrent clients will appear here, based on your seedbox username.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469102256.PNG)

You can also add a new external connection by choosing the last option. This will open a new modal which you can use to set your external deluge, rtorrent or qbittorent client. 

For rTorrent:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469200153.PNG)

For Deluge:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469227173.PNG)

For Transmission:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1715247474870.37.26.jpg)

For Qbittorent:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1683614941623.jpg)

Lastly, by clicking the **three dots** icon, you can make a connection default or edit/delete any external connections you previously added. You can't edit/delete the torrent clients associated with your seedbox(es)

**NOTE:** Transmission is not currently supported.

### Edit Torrent

If you click **Edit Torrent** from the torrent menu actions then you will see the following modal:

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468705239.PNG)

Just change whatever you need, click **Edit** and your torrent will be updated with the new values!


### Speed Limit

If you click **Speed Limit** from the torrent menu actions on Deluge you will see the following submenu
where you can adjust the torrent's speed limit by dragging the slider or by typing the desired value.

**NOTE:** Your changes will be applied when you close the context menu .

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1536835830797.png)

### Search
In the top of your torrent list you will find the search input from where you can filter your torrent list and see immediately all results. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468768188.PNG)

### Torrent Details

**General**

Useful generic information about the selected torrent.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468781431.PNG)

**Files**

The torrent file tree with useful information, such as the current progress of the file. In addition, for each file there is an action menu (just right click on a file or click the three dots in the last column if you are in mobile view).  

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468819230.PNG)

**NOTE:** if you are connecting to a Deluge daemon then there is no action menu.

**Trackers**

A list of all associated trackers with this torrent.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468827953.PNG)

If you notice on the screenshot above, there is a small **lock** icon which indicates that the torrent tracker is private. 

**Peers**

A list of connected peers while leeching/seeding.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468855049.PNG)

### Torrent Client Settings

To modify your torrent client settings, navigate to Torrent Client Settings by clicking the **gears** icon located on the main toolbar at the top right section of the screen. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468916176.PNG)

As you will see, your torrent client settings have their default values. Of course, feel free to modify them any time.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643468944231.PNG)

For Qbittorent, there are some more options you can fiddle with;
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1683615048709.jpg)

In  torrent client settings you can:

* Set your default download path
* Enable watch folder and set your watchfolder's path. This means that if you drop any **.torrent** files inside that folder, the torrent client will automatically pick it up and send it to your torrent client. Qbittorent supports multiple watch folders
* Enable option for autostart torrents after they are imported
* Enable move completed files and set the path where your files will be moved after completion
* Add categories (Qbittorent only) so you can easily set different completed folders for your torrents
* Change your torrent client's global upload and download limits with the slider or by typing
* Enable DHT Network
* Enable Peer Exchange

### Uploading

The easiest way is to drag 'n' drop your **.torrent** file at your torrent client dashboard list. The upper section is used for immediate start of the torrent once it gets added while the bottom section is used for paused stated

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469708275.PNG)

You can also easily upload torrents to your torrent client by simply clicking the **plus** icon from the main toolbar.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469510929.PNG)

The following modal will appear which will allows you to either upload **.torrent** files or you can add a torrent using a **magnet url**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469548309.PNG)

For Qbittorent, another field will be shown for your category. Also, multiple labels can be input for this torrent client
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1683615256662.jpg)

There are a few options you could use when uploading such as:

* **Start automatically:** By default the torrent(s) will be started as soon as upload completes. Toggle off to add them in Paused state
* **Select download path:** If you do not wish the default torrent client save path to be used, set your path here and will be used for all uploaded torrents
* **Categories:** You can choose a category so torrents upon completion can be moved to the folder set at the category. Categories need to be already pre-created via the torrent client settings
* **Label:** Automatically add a new label by clicking inside the text field or choose an existing label from the dropdown menu. For Qbittorent only, this is called **Labels** and you can set multiple labels for a single torrent

### Labels

**Adding new labels** to torrents is very easy.

Right click on your selected torrent and then click on the "Add Label..." menu. The menu itself is a text field, so once you click it a caret is going to start flashing and you can start typing. Once finished you can press Enter or click the "Add" on the right side. The label will appear on the left side of the torrent's name.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469740494.PNG)

**Existing labels** will appear on the right side of the "Add Label..." when you hover it so you can quicly add them to your selected torrents. You can also remove labels from the selected torrents by selecting "None"

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469778362.PNG)

You can also modify the color of the label to the one you prefer

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469784134.PNG)

### Bottom bar

In torrent client there is a bottom bar where there are various global controls and statistics.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469802114.PNG)

These are:
* Your global download and upload speed
* an input where you can see and change your global upload and download speed limits
* your total uploaded and downloaded bytes
* Seedbucket version as well as torrent client version by clicking on the info popup in the right end of the bottom bar

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469901030.PNG)

You can click the **Show changelog** and a modal will appear will the latest changelog

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1643469949690.PNG)

You can change speed limits just by clicking on the speed limit value you want(upload or download) and modify it by slider or by typing in the input that will appear.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1536833607251.png)

