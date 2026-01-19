---
id: how-to-connect-via-ftp-to-your-account-using-filezilla
title: How to connect via FTP to your account using FileZilla
description: Learn how to connect to your seedbox account via FTP using FileZilla with this step-by-step guide.
keywords:
    - FTP
    - FileZilla
    - seedbox
    - connect via FTP
    - FileZilla configuration
---

# How to connect via FTP to your account using Filezilla

[FileZilla](https://filezilla-project.org), is a neat and lightweight ftp **client**, which is available for Windows, MacOSX and Linux

We made it very simple to configure it, and it is simple to use.

In detail:

* Download and install FileZilla
* Login to your [client area](https://www.seedboxes.cc/dashboard). After you log in to your seedbox account, click in the "My Client Area" button.

![file](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/a26847ea-a04d-4fe9-b283-ecb5108404b3.png)

* Select the seedbox you are interested in from the **"My Seedboxes"** list.

![client_area_select seedbox.png](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/a7d33c23-234c-47af-aaa0-68b39f72a763.png)

* Scroll down to the **"Connection Details"**. At the **"FTP"** section you will see a **"Download Filezilla Configuration"** button. Press it and you should download a **"sites.xml"** file.

![ftp.png](https://s3.eu-central-1.amazonaws.com/rapiddot-support-community-uploads/feaf6a52-5a8e-4bd8-8f36-1ff60a917814.png)

* Open FileZilla, and go to Settings. In the Transfer options set the Maximum simultaneous transfer to "3"

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491560892972.png)

* Go to File > Import
* Choose the file **"sites.xml"**  that you just downloaded when FileZilla will ask for confirmation to import the Site Listings, choose OK
* After you receive a successful message, that the import is complete, go to File > SiteManager

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1598953415041.png)

* Choose the entry with your servername, and click "Connect"

:::info Note

Filezilla doesn't support multi-segmented downloading (which is different from simultaneous transferring).
If you need multi-segmented downloading, in order to maximize your FTP download speed, then refer to [this](./Optimize_FTP_downloads_from_your_seedbox_with_multi-part__multi-segmented__downloading.md) guide

:::

:::info Note 2 
Due to some changes from our end, FTP now can show hidden files and folders (as SFTP does). Some FTP clients support hiding/showing hidden files from their settings (like Cyberduck for example). Unfortunately Filezilla doesn't natively support that setting, so if you want to hide the hidden files in Filezilla, you must do the following;
* Create a **Directory listing filter** (from the top menu **View -> Directory listing filters**) then click on **Edit filter rules..** (bottom left, check the first screenshot below)
* Create a **new** filter and name it e.g. "Hide hidden files". At the filter conditions, select **Filter out items matching all of the following** and the first condition should be **Filename**, **begins with**, **.** (point character, as shown at the second screenshot) and click **OK**
* From the previous window, **enable** the filter on the right side (**Remote filters**)
* Click **OK** so you can now apply that custom filter you just created
:::

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1674550517726.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1674550524261.png)