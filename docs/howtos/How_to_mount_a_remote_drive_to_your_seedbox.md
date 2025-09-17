---
id: how-to-mount-remote-drive
title: How to mount a remote drive to your seedbox
description: Learn how to mount Google Drive, Dropbox, or S3 to your seedbox using rclone for seamless integration with apps like Sonarr and Radarr.
keywords:
    - seedbox
    - remote drive
    - Google Drive
    - Dropbox
    - S3
    - rclone
    - mount
    - Sonarr
    - Radarr
---

# How to mount a remote drive to your seedbox

## Introduction

Based on our most recent seedbucket survey, one of the things you requested was to be able to mount your Google drive to your seedbox so other apps (e.g. sonarr, radarr etc) can also have access to it.

We **heard** you!

You are now able to create a remote mount point for your **Google drive**,  **Dropbox** or **S3** (**crypt storage drive** included) and use that mount in other apps too.

**NOTE:** If you want another drive to be mounted, it must be officially supported by rclone. Just open a ticket from your client area, sending us a working rclone configuration for that drive and we will mount it

**IMPORTANT: Have in mind that mounting your remote drive in your seedbox, requires the use of a local file cache (located in your seedbox) to speedup the performance of the mount and minimize the API calls to the Google drive API (to reduce the chance for you to hit limits that could result in a ban of your Google drive account).
This cache can grow up to 200GB in storage in your account (depending on the frequency of reading/writing on the mount), so please bear in mind to have this space available in your seedbox before activating your mount**

**ALSO IMPORTANT: AVOID setting your download clients (torrent client, sabnzbd / nzbget) to download DIRECTLY to your mount, as this will cause very slow network speeds, your apps/clients becoming unresponsive/inaccessible and most probably hitting an API limit / ban. The correct procedure is to download locally to your seedbox and set your paths at sonarr/radarr apps towards your mount, so only finalised content is uploaded. You can check for further details [here](../howtos/How_to_use_sonarr_and_radarr_with_your_remote_mount.md)**

## Installation

The installation process is done via our **Seedbucket** app and it is based on rclone functionality.
**Note:** You need to have already added a Google drive, Dropbox or S3 to your seedbucket. If you also have a crypt drive (for that Google, Dropbox or S3 drive) with existing encrypted content or if you want to create a new crypt drive from scratch so that the mount point contains encrypted content from that moment and on, you need to do so **before** creating the rclone mount point.
You can find more information regarding the encryption section in our seedbucket guide [here](../seedbucket/How_to_use_Seedbucket.md#encryption) .

Just head to your **Settings -> Apps** section. To do so, click at the top right corner your email address and at the dropdown menu, click the **"Settings"** link.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1641545459773.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1641545464589.PNG)

At the settings page, click the 3rd tab labelled **"Apps"** .

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1641545664660.PNG)

If you have more than one seedbox, you need to select the seedbox from the dropdown menu, in order for the remote point to be mounted at that selected seedbox.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639731636422.PNG)

Once the seedbox is selected, click the **"+ Install"** button so you can begin the process of creating the mount point

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639731743671.PNG)

**NOTE: Bat Box and Gremlin Box can mount a SINGLE remote point. Vampire Box and better tier seedboxes get an additional remote point available to be installed and mounted, as shown at the screenshot below.**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639731769316.PNG)

### Google mount

**First step:**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518409120.16.11.jpg)

Select a Google drive storage from the dropdown menu. If you have many drives, just scroll down until you find the one you want and click the **Next** button

**Note:** If you want to perform the mount at a specific folder instead of your whole drive, just navigate to that folder and click the **Next** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518480144.16.21.jpg)

**Step 2/5:**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639723692155.PNG)

You need to log into [Google API Console](https://console.developers.google.com/) with the Google account you previously selected and either select an existing project or create a new one and select that afterwards.

**Note**: If this is your first time in the API Console, you need to accept the Terms of service, agree and continue

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1555926843344.png)

Select a project in the dropdown menu on the top left **Select a project** or create a new one via the **Create** button on the top right corner
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573650778953.png)

**Note**: If you have already created projects in the past and you create a new project for the Google drive integration, **don't forget to select** the project after it is created, as it doesn't get automatically selected!

Click the link **+ ENABLE APIS AND SERVICES** as shown in the screenshot, which you find at the **Dashboard** left menu 
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573652137177.png)

Type the word **Drive** at the input field, choose **Google Drive API** and click **ENABLE**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1555332650573.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573652298265.png)

**Step 3/5:**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639724524755.PNG)

You need to configure the **"OAuth Consent Screen"**. If you have already configured it in the past (make sure that you have set User type to **"External"** and have **Published** the app), you can skip this step. Else:

Click **OAuth consent screen** at the left side panel. There might be an extra option whether you want internal (restricted) or external (public) type of access. Choose **External** user and click the create button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1573652540969.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1574593155308.png)

Type an application name of your choice, choose your email from the **User support email** dropdown menu, type your email address at the **Developer contact information** (can be the same user email) at the bottom of the page and click the **SAVE AND CONTINUE** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614271438240.png)

At the next screens (**Scopes** and **Test users** ), leave everything default and click the **SAVE AND CONTINUE** button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614271777665.png)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614271788714.png)

At the final screen you should see the **Summary** 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614271916377.png)

Now click again the **OAuth Content Screen** at the left panel

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614272006225.png)

Click the **PUBLISH APP** button and at the new modal, click the **Confirm** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1614272106524.png)

**NOTE: MAKE SURE YOU CLICK AT THE "PUBLISH APP" LINK. IF YOU DON'T, IT WILL REMAIN AT TESTING STATUS WHICH WILL BE VALID FOR A WEEK. AFTER THAT, THE TOKEN WILL AUTOMATICALLY EXPIRE**

**Step 4/5:**
Click the copy **icon** so that the URI that is needed afterwards is copied to clipboard.
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639727115489.PNG)

Back at your Google drive console, click **Credentials** at the left side panel and then the **+ CREATE CREDENTIALS**. At the dropdown menu, choose the **OAuth client ID**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639726134622.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639726209836.PNG)

For the **Application type**, choose **Web application**. Give it a name and paste the link you previously copied under the **"Authorized redirect URIs"** section and press the **CREATE** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639726305996.PNG)

**IMPORTANT: If you have created a project in the past with application type "Other" or "TV's and limited input devices", you need to create new credentials with the correct type -Web application- and paste the URI at the "Authorized redirect URIs"**

**Step 5/5:**
Once the OAuth client is created , the **Client ID** and **Client secret** will be created
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639747848238.png)

Just copy and paste them from your Google console back to your seedbucket app and click the **Authorize and Install** button.
**NOTE:** Make **sure** that both fields are copied and pasted correctly!

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639726504367.PNG)

**IMPORTANT:** Since the app you just created is not verified (and this is totally normal), you need to click the **"Advanced"** button at the new screen in order to reveal the link to **"Go to seedboxes.cc (unsafe)"**, so you can finish the mount installation.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640096961465.PNG)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1640096969631.PNG)

### Dropbox mount

**NOTE: Dropbox team/business folders reside at the root level of dropbox, so if you want to have access to your team folders, you need to perform the mount at the root level**

**Step 1/4**:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518608770.22.38.jpg)

Select a Dropbox drive storage from the dropdown menu. If you have many drives, just scroll down until you find the one you want and click the **Next** button.

If you want to mount your dropbox at a specific folder, just navigate to that folder and click the **Next** button
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518697460.23.09.jpg)

**Step 2/4**:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639728375694.PNG)

You need to log into [Dropbox App console](https://www.dropbox.com/developers/apps/create) with the Dropbox account you previously selected. That link automatically redirects you to the create app process. Choose the **Scoped access** (which currently is the only option)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639728605523.PNG)

**Step 3/4**:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1685460068670.31.46.jpg)

By selecting the **Scoped access**, the type of access will be revealed. Choose **Full Dropbox** so rclone can access all of your files. Name your application to something unique as this is a global name and click the **"Create app"**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639728617483.PNG)

You will be redirected to the app's settings page. Click the **"Permissions"** tab
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639729453138.PNG)

You need to enable the following permissions:
> **account_info.read**
> **files.metadata.write**
> **files.content.write**
> **files.content.read**
> **sharing.write**

The **files.metadata.read** and **sharing.read** checkboxes will be automatically marked as enabled.
Click the **Submit** button at the bottom page once ready.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639729506368.PNG)

**NOTE: YOU NEED TO ACCEPT DROPBOX COOKIES IN ORDER FOR THE *Submit* BUTTON TO BE REVEALED**

**Step 4/4**:
At your seedbucket, click the copy **icon** so you copy to clipboard the URL that is going to be needed aftewards.
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639730606549.PNG)

Switch back to the **"Settings"** tab. At the **"OAuth2 - Redirect URIs"** paste the link that was previously copied to clipboard and click the **Add** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639730706934.PNG)

You should see something like this:
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639731084449.PNG)

Finally, copy the **App key** and **App secret** (just click the "Show" link so it can be revealed) back to your seedbucket app and click the **"Authorize and Install"** button.
**NOTE:** Copying the **App secret** might not work properly. You need to hold the mouse button while selecting the text, copying it with ctrl-c then releasing the mouse button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1639731045691.PNG)

### S3 mount

S3 mounts don't require any kind of further authorization, therefore just select the drive (for root) or any of its folder in order to be mounted

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1705042008742.45.19.jpg)

### Crypt drive mount

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518896021.27.57.jpg)

Select a crypt drive storage from the dropdown menu. If you have many drives, just scroll down until you find the one you want and click the **Next** button

If you want to mount your crypt drive at a specific folder, just navigate to that folder and click the **Next** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1659518910185.28.09.jpg)

Please check either the Google, Dropbox or S3 mount instructions above. Based on the storage drive that the crypt drive was associated to, the guidelines are exactly the same.

## Mount path

After installation is finished, navigate to your apps (e.g. sonarr, radarr etc). You can find the mount at **/home/user/mounts/rclone/** and **/home/user/mounts/rclone2/** (for seedboxes that support two mount points).

That was it! Apps can now access the mount point(s) !