# How to setup Unpackerr with UnpackerrUI on your seedbox

## Introduction

From the official unpackerr [github](https://github.com/Unpackerr/unpackerr):
> *Unpackerr runs as a daemon on your download host or seedbox. It checks for completed downloads and extracts them so Lidarr, Radarr, Readarr, and Sonarr may import them. If your problem is rar files getting stuck in your activity queue, then this is your solution.
Not a starr app user, and just need to extract files? We do that too. This application can run standalone and extract files found in a "watch" folder. In other words, you can configure this application to watch your download folder, and it will happily extract everything you download.
Interested? Check out the website with installation instructions:*

We decided not only to implement this daemon but to also write a GUI from scratch for it, so it is easier for the users to interact and set it up.

In this guide, we will be showing how to use it with all "Starr" apps we support (Lidarr, Radarr, Readarr, Sonarr and Whisparr) as well as -optionally- how to set up custom watch folders so you can automatically extract compressed files in those watched folders, regardless of any apps.

**Note:** The Starr apps don't support autoextracting compressed files, so if you download a torrent that has e.g. rar files in it, they won't be able to decompress them and they will be shown as "grabbed" only. With the exception of rutorrent v3, other torrent clients don't have the ability/plugins to extract files.
Therefore, this is where the unpackerr app shines and comes in handy 


## Installation
Go to your client area, click the **Installable Apps** section and add unpackerr via **+Add Application** button. You can find a more detailed guide regarding 1-click installation of the apps [here](./How_to_install_our_1-Click_applications.md). 

After unpackerr installation from your client area, open the link to navigate to the app. You will be asked to sign in with your seedbox credentials, as with any other app.


### Connect Starr apps

#### Automatically

After login, you will see at a list all of your Starr apps that are already installed at your seedbox. For example, if you have installed Lidarr, Radarr and Sonarr, you will automatically see all three of them.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708440061140.39.06.jpg)

:::note
Of course, the word USERNAME will be automatically replaced with your current seedbox username.
Also, if you decide later on to install another Starr app, it will be automatically shown at the list.
:::

You can simply add the daemon to any of the apps by clicking the **Add** button for that particular app

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708087235755.39.51.jpg)

Once you click the add button, the daemon will be set to be installed for that app after you click the **Apply Changes** button at the top right corner of your screen



:::warning IMPORTANT 
Don't forget to click the "Apply Changes" button at the top right corner of your screen so you can apply those adds/changes to the daemon**
:::

You can of course edit (for extra options) or delete the daemon if you no longer use it

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708088374475.38.06.jpg)


If you click the **Edit** button, you can set/modify the API key, the app URL as well as the download paths.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708093082643.38.55.jpg)

:::note
This is **NOT** the root path of your Starr apps, this is the download directory of your torrent client. You probably use the default which means that you won't have to edit the path in the first place.
However if you have set a custom download path at your torrent client settings, you also need to edit (or append) that path to the form.
As with adding the daemon for any app, don't forget to click the **Apply Changes** button at the top right corner so all changes can be in effect.
:::

#### Manually

We also give you the option to add your Starr app manually. Just click the **"+"** button at the right section of the **App** row. At the new modal, select the type of the Starr app and input all necessary information. The text area gives you hints regarding which URL and Paths to use. As for the API key, you need to navigate to your Starr app and go to settings -> general

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708099925859.11.23.jpg)

### Set custom watch folders

You can also set the unpackerr daemon to watch custom folders of your choice. This is useful e.g. for games that have many compressed files. Just click the **"+"** icon at the right section of the **Watched Folders** row

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708094105705.06.35.jpg)

At the pop-up menu, you can set the watch folder path at the **Folder path** input.
Optionally, you can set the extract path to be another path of your choice at the **Extract path** input. Leave it blank if you want the extract path to be the same as the watched folder path. 

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1708094128203.07.21.jpg)

By default, all files are kept as they are.
If you need the daemon to delete files (either the extracted or the original), you must first set up a timer for files to be deleted after that duration and then choose from the options below;

- **Disable recursion**: If this is enabled, unpackerr extracts archives inside the archive
- **Delete files**: If this is enabled, delete extracted files after successful extraction
- **Delete Original**: If this is enabled, delete original items after successful extraction
- **Move Back**: If this is enabled, move extracted files into original folder. If this is disabled, files go into an \_unpackerred folder
- **Extract ISOs**: If this is enabled, the app will extract ISO files with .iso extension