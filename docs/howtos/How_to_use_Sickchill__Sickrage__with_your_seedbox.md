# How to use Sickrage with your seedbox

## Introduction
Sickchill (Sickrage) app offers a very nice functionality for your shows as *It watches for new episodes of your favorite shows and when they are posted it downloads them, sorts and renames them, and optionally generates metadata for them* .
That means that you can easily automate the process of extracting the downloaded files, renaming the episode, move it to the appropriate folder and search for subtitles.

## Installation

1) [Install Sickchill (Sickrage) from your client area](./How_to_install_our_1-Click_applications.md)

2) Hover your mouse on the **gears** icon at the top right corner and choose **General** from the dropdown menu.
At the new window, scroll down and at the **Show root directories** option, click the **New** button and choose where the files of shows are located.
Click **New**, and input (or navigate to) ;
> /home/user/files/Plex/TV 

Click **Save changes** button and again, **Save changes** at the bottom left corner.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559214520888.png)

**NOTE**: The path `/home/user/files/Plex/TV` is being chosen so you can can implement at a future time the same folder for your plex server app too, should you choose to install it.
Also, bear in mind that if the folder doesn't exist, you have to manually create it, either via your Seedbucket app (an excellent guide on how to use the app is [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket)) or through SSH

3) Hover your mouse on the **gears** icon again, this time choosing **Search providers**.
You will be automatically redifrected to the first tab **Provider Priorities**.
From the tracker list, tick to enable the tracker(s) you wish to use. Scroll at the bottom and click **Save changes** button.
Press **F5** or refresh the page. You will now see all the chosen trackers to be up in the list, prioritized. You can **drag and drop** a certain tracker if you wish to change its priority - don't forget to click **Save changes** button again.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559215847390.png)

4) Head to the second tab **Provider Options** and set your login credentials for each private tracker you chose at the previous step.
Click **Save changes** button at bottom left corner

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559216224837.png)

5) Once more, head to the **gears** icon at the top right corner and select **Subtitle settings**.
Enable the option for searching subtitles and choose the subtitles language of your liking

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558528590344.png)

Don't forget to **Save changes** at the bottom left corner!

6) Go to the second tab **Subtitles Plugin** and choose the subtitle services you wish to use, by ticking and prioritizing them, like you did at the trackers list.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1559216961789.png)

Again, don't forget to **Save changes** at the bottom left corner!

7) If you chose a subtitle service that needs login credentials, you can do that a the third tab of the subtitles section, **Plugin Settings**.

8) Finally, head to the **gears** icon and select **Post-Processing**.
At the first tab (**Post-Processing**), tick the option for enabling the automatic post processor and set the corresponding path, as in the screenshot. As for the processing method, you can choose **Copy** method that will copy the downloaded files to the location specified, thus enabling you to keep seeding torrents after they are finished

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531271932.png)

Scroll down and choose to **unpack (process contents)** as well as the other settings as shown at the screenshot.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531283140.png)

Don't forget to **Save changes** at the bottom left corner!

## Add shows

All previous steps regarding configuration and options are done only once.
Now you are ready to start adding your favourite shows. Hover your mouse on **Shows** at top right corner and choose **Add Shows** from the dropdown menu

Input the show's name and, click the **Search** button and pick a show (click the bullet!) at step #2. The folder will already have been picked by default as it was set at the previous steps.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1627048821069.png)

Scroll down for more options, choose your preferred **quality** and the status of **previous / future** episodes. Click **Add Show** at the bottom left corner
**Note**: You can save those options as **default** so you don't have to change them again in the future for other shows

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1558531490573.png)

The show will be added and it will automatically start downloading the files when the episode is aired, post-process them (extract/rename/move) and search for subtitles. Rinse and repeat for your following series-to-add!