## Introduction

A personal NAS server is an alternate solution to stream media content locally.
You can combine;

1. the very fast network speeds that the seedbox provides you (for your downloads as well as secure transfers towards your NAS via FTPS), with
2. streaming locally (meaning in the same network as your NAS) to any media client (plex/emby/jellyfin etc) connected to your local network



So in case of your ISP throttling the connections or just being congested (mostly at evening/peak hours), you have now the option to enjoy -without any buffering/disconnects- the content you want to stream as it will already be available offline via your NAS.

The only drawback of course is that the NAS server must be up-and-running 24/7 in order to receive the transfers from your seedbox as well as being able to stream locally.
Plus, it requires four steps (easy to perform) in order to set everything up succesfully - thankfully this is a only one time thing. You should only focus on what to download, not how to download it :) 

## Setup

### Enable FTPS

The first step is to enable the FTPS access on your NAS. Since there are many NAS OS and/or NAS devices, it is impossible to include a guide for all of them. The most popular is the synology, you can find a guide for that [here](https://kb.synology.com/en-global/DSM/tutorial/How_to_access_files_on_Synology_NAS_via_FTP).
For any other OS/device, a google search will suffice.

The general idea is the same, you should navigate to the NAS settings and enable the FTP access so outer networks can connect to your own, using encryption.
Just make sure to **ENABLE TLS/SSL ENCRYPTION (also known as FTPS)**, in order to make transfers encrypted from your seedbox towards your NAS

### Add FTP drive to seedbucket

The second step is to add the NAS server via FTP to your seedbucket dashboard. You can check our guide for that [here](https://community.seedboxes.cc/articles/how-to-use-seedbucket#ftp).
Make sure to enable (toggle) the **Secure** and **Use authentication** buttons for encryption and inputting your credentials (host / port / username / password) at the necessary fields, according to that guide.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716207282372.14.28.jpg)

Once you add it to your seedbucket, copy a file towards that FTP dashboard and navigate to it in order to check that everything works perfectly (meaning you have set up correctly your NAS server to accept incoming connections from our network)

### Add media indexers

The third step is to add media indexers at your seedbucket. These are essentially tools to automatically search and download torrent files, based on your media needs.
You can easily do that via settings -> media . Just click the **Add media indexer** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1718878583008.16.09.jpg)

A modal will emerge on your screen so you can select the indexer of your choice

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716202200276.09.16.jpg)

You have the option to either search for all available indexers, or filter them by their privacy (public, semi-private or private indexers). Public indexers don't require a username/password, nor care about ratio but might lack in download speeds, in contrast with private indexers.

**IMPORTANT: If you want to use private indexers, BE WARNED THAT THIS WILL BE RECEIVED AS A HIT-AND-RUN due to the fact that after the torrent finishes downloading, it gets automatically deleted (so no seeding afterwards). Unless you are a VIP at that private indexer (or that indexer doesn't care about your ratio), you should avoid using these kind of indexers as you will be probably BANNED from accessing and using them in the future.**

So the safe bet is to always use a public indexer, that is widely known too (e.g. 1337x). Just be certain to fill out any necessary fields (like Base Url, which is easily selected via a drop-down menu), then click the **Test** button on the bottom left corner to check if everything is fine and lastly click the **Add Indexer** button on the bottom right corner. Be warned that if there is a seed ratio field, this will be IGNORED as stated at the screenshot.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716207556154.18.42.jpg)

**Note**: For the time being, indexers are used sequentially (meaning in added order). If the first indexer can't find the data, it automatically moves to the second etc. It is in our TODO list to easily change the indexer order via dragging them to the top/bottom, just stay tuned for the next seedbucket version coming soon!

**Note2**: You can also see that certain quality profiles are already pre-created for you and they should cover any quality needs you have. Feel free to check the relevant [section](https://community.seedboxes.cc/articles/how-to-use-seedbucket#quality-profiles) at our seedbucket guide for that, in case you want to make any adjustments

### Add Libraries

Last but not least, the fourth step is to create movie and tv libraries for your media content.
Just click the **Library** dashboard. As you can see, you haven't created yet any libraries

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716208123376.28.18.jpg)

Go ahead then and click the **Add Library** button. You will be greeted with a new modal.
You must type or choose **a)** the name for your library, **b)** its type (Movies / TV) and **c)** the Save path (or paths) for that type.
For example, let's say at your NAS FTP you have a library path for your movies at /media/Movies. By performing the above, you should see something like that;
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716208054852.21.37.jpg)

Of course, you can have multiple paths for the same libray and multiple libraries for the same type! The possibilities are endless!

## Download media

Once you have finished setting all of the four steps above, you are now ready to discover and add any media at your libraries.
Everytime you log in to seedbucket, you will be automatically navigated to the **Discover** dashboard in order to explore and discover movies and TV shows that you might like, read information about them, watch trailers (if supported) and more, similar to how IMDB works, but without leaving the app!
You can of course search for content inside the bar that resides at the top middle section of your screen.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716209944902.58.56.jpg)

If you click inside a title, you will see many details regarding that movie/series, like who is the director/producer, who are the cast, as well as recommendations or similar titles.
At the right section of the screen, there is a button **Watch Trailer**, which as the phrase states, opens an in-browser youtube video with the trailer of that title.
There is also an **Add to Library** button which you can easily add the title to your media library you created at the previous step.

For example, let's say you want to download the [publicly available -free of any rights-](https://archive.org/details/the-house-i-live-in-1945) movie called "The House I Live in" produced in 1945 . Just type that title to the search bar and all the results will appear

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716210557779.01.24.jpg)

What you want is the second movie, just hover your mouse to check the release date and once you confirm this is it, click it to check its details

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716210624578.09.58.jpg)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716210756413.12.05.jpg)

At the right section of the screen, click the **Add to Library** button. A new modal will appear.
If you have only one library, that will be already preselected. Same goes for the save path.
If not, just choose it from the drop-down menus.

From the **Profiles**, choose the corresponding quality profile you want to use.

If you want to **Monitor** that release, just choose that option, again from the drop-down menu.
Note: You can hove your mouse at the **i** icon for more information regarding the Monitoring statuses and their differences (mostly found in series).

Lastly, the **Search and download** toggle button is already pre-enabled so once you add that movie to your library, it will immediately search the indexers to download it. The download depends on the quality profile and on the number of seeders.
In case you don't select it (note: this option is missing in series so you can check what seasons / episodes to download prior to downloading everything!), this will just add the media item to your library, without downloading its data.
You should see something like this in the end;

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1716210991843.16.17.jpg)

If you click the **Add to Library** button, it will be successfully added to that particular library and the indexer will immediately start seaching for it. 

For TV Series, the process is almost similar. The only thing that changes is that there is no **"Search and download"** button when you are about to add the series to your library.
Instead, there are more options to the **"Monitor"** field - if you hover your mouse button, you can see some relevant information. The default "upcoming" should cover most of your needs, which means it will automatically download future episodes when they get released.

Once you add the series to your library, you will have the option to download any previous releases by clicking the **Request to download** button on the same row as the "Season".
You also have the option to download per-episode, in which case you should either click the **Request to download** button at the episode's row OR the **Interactive search** button (resembled as a magnifying glass, under Actions) so you can manually select which release to download

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1718880812874.28.47.jpg)

That's it!
