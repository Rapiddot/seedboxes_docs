---
title: "Seedbucket Changelog"
id: "seedbucket-changelog"
description: "This document provides a detailed changelog for all versions of Seedbucket"
keywords:
    - seedbucket
    - changelog
    - software development
---

# Seedbucket Changelog

### **Version 2.3.1 (10/Feb/2020)**

* **[Bugfix]** Fix issue with file size not updating properly in file browser
* **[Bugfix]** Fix issue with file type not updating properly in file browser
* **[Bugfix]** Fix issue with file sharing and predefined folders not updating properly
* **[Bugfix]** Fix issue when uploading to an encrypted folder
* **[Bugfix]** Fix issue with huge file sets and hidden files that sometimes caused the underlying service to crash

### **Version 2.3.0 (29/Jan/2020)**

* **[Feature]** Implement crypts manager and the ability to re-use them on different folders
* **[Feature]** Implement uploading/downloading from encrypted folders
* **[Improvement]** Re-design dashboards list in settings
* **[Improvement]** Re-design breadcrumbs and make them cleaner and smoother
* **[Improvement]** Silent indexing when visiting existing folders instead of blocking UI
* **[Improvement]** Major performance improvements with copy/move and general experience
* **[Improvement]** Major performance improvements with file system watching
* **[Improvement]** Misc UI fixes and improvements
* **[Bugfix]** Fix issue with dashboard url path reset
* **[Bugfix]** Fix issue with empty password/salt when creating a new crypt
* **[Bugfix]** Fix issue when sorting by size in file browser
* **[Bugfix]** Fix issue when trying to delete dashboards that are no longer connected to an adapter

### **Version 2.2.3 (25/Nov/2019)**

* **[Feature]** Implement Rclone support
* **[Feature]** Implement Rclone configuration export functionality
* **[Feature]** Implement Plex installer that can be configured with Google Drive and Rclone
* **[Feature]** Implement keyboard shorcuts for selecting/deselecting all files and creating new folder in file browser
* **[Feature]** Allow users to create a new file browser dashboard with a custom home folder from any drive
* **[Improvement]** Improve application loading time
* **[Improvement]** Show modal when user tries to add an existing predefined folder with actionable options
* **[Improvement]** Full file title should shown on mouse hover in file list
* **[Improvement]** Sort folders by name in copy/move modal
* **[Improvement]** Fix cropping of all characters after dot when compressing archives in file browser
* **[Improvement]** Distinguish Google Drive from Google Team drives
* **[Improvement]** Replace adapter icons with colored ones
* **[Improvement]** Refactor file browser in order to use id urls instead of folder paths
* **[Improvement]** Show "Version Changelog" modal after each update and on user request
* **[Improvement]** Show application error information when pre-loader fails
* **[Improvement]** Convert file browser "move" action to job for better performance
* **[Improvement]** Improve transfer speed accuracy when copying files
* **[Bugfix]** Fix issue with 'last updated' column in torrent list
* **[Bugfix]** Fix issue with indexer status getting stuck forever in "IN PROGRESS"
* **[Bugfix]** Fix issue when adding a torrent from an external drive to the torrent client
* **[Bugfix]** Fix issue with google team drives and wrong disk space validation
* **[Bugfix]** Fix issue with torrent getting unselected while drawer is open and clicking anywhere within the drawer
* **[Bugfix]** Fix issue with context menu within torrent client container drawer lists containing wrong actions
* **[Bugfix]** Fix minor issue when sorting torrents by status
* **[Bugfix]** Fix issue with some FTP servers returning empty strings in their listing response
* **[Bugfix]** Fix issue when using existing labels with torrent uploading and rTorrent 
* **[Bugfix]** Fix issue with Dropzone and file name titles overlapping when too wide
* **[Bugfix]** Fix issue with FTP/SFTP listing and invalid folder path
* **[Bugfix]** Fix issue with folders that belong to root not appearing in search results
* **[Bugfix]** Fix issue with ENTER key not triggering primary action in a few modals
* **[Bugfix]** Fix issue with editing torrents and setting torrent files priority in ruTorrent
* **[Bugfix]** Fix issue with download speed indication in torrent client when using Deluge
* **[Bugfix]** Fix issue with google team drives and file deletion when user has no permission to delete; move to trash instead
* **[Bugfix]** Fix issue with chunked downloading from local storage

### **Version 2.0.0 (20/Jun/2019)**

* [**Feature**] Implement Global Search
* [**Feature**] Implement support for Google Team drives
* [**Feature**] Allow users to choose the file size format when adding FTP/SFTP drives
* [**Feature**] Allow users to pre-select archive extraction write mode (skip vs overwrite)
* [**Feature**] Allow users to create/extract password protected archives
* [**Improvement**] Support resumable download links for FTP, SFTP and HTTP
* [**Improvement**] Enable downloading from FTP/SFTP adapters
* [**Improvement**] Re-design modals for mobile devices
* [**Improvement**] Smoother UI and misc bug fixes for all devices
* [**Improvement**] Enable file browser folder selection in tablet view
* [**Improvement**] Show modal with options for soft or hard index before running local adapter indexer
* [**Improvement**] Replace all file list icons with custom ones 
* [**Improvement**] User adapter icons for starred folders list
* [**Improvement**] Support local copies/moves within the same adapter for faster execution
* [**Bugfix**] Fix issue when adding torrent and setting new location that contains multiple spaces in file name
* [**Bugfix**] Fix issue in torrent client that caused error while the list was loading when a torrents tracker url was missing
* [**Bugfix**] Fix issue when deleting a drive did not delete it's associated dashboards
* [**Bugfix**] Fix alignment issue with disk space component in case of 'unlimited' drive storage
* [**Bugfix**] Fix issue with file sharing when a custom home path was used in FTP and SFTP drives
* [**Bugfix**] Fix issue when trying to upload multiple torrent files and selecting a custom save path
* [**Bugfix**] Fix issue with "Add torrent" dropzone disappearing after file type error
* [**Bugfix**] Fix issue with extract archive modal text area and unlimited expanding
* [**Bugfix**] Fix issue when extracting files and pre-existing folders
* [**Bugfix**] Fix issue with file uploading and UTF8 file names that appeared as jibberish
* [**Bugfix**] Fix issue with handling of different special characters for each storage drive
* [**Bugfix**] Fix issue with predefined folders and same folder path
* [**Bugfix**] Fix compatibility issue with Firefox for iOS
* [**Bugfix**] Fix issue with indexing gif remaining even after indexing is done
* [**Bugfix**] Fix issue with file list and missing results from Google Drive when maximum number of items per request is reached

### **Version 1.8.3 (03/Dec/2018)**

* [**Bugfix**] Fix bug with stucked jobs while copying files to Dropbox and OneDrive
* [**Bugfix**] Fix bug which prevented file or folder deletion in SFTP adapters
* [**Bugfix**] Fix bug when moving files with any adapter in file browser that caused failure

### **Version 1.8.1 (19/Nov/2018)**

* [**Feature**] Implement file browser bottom bar 
* [**Feature**] Implement predefined folders for quicker access when copying/moving files
* [**Feature**] Implement dedicated abort button per file when uploading
* [**Improvement**] Simpler modal for folder selection instead of tree view
* [**Improvement**] Simpler breadcrumbs that can handle deep folder levels 
* [**Improvement**] Better disk space indicator 
* [**Improvement**] Better and more robust jobs system for copying files and other tasks 
* [**Improvement**] Smoother UI and misc bug fixes for all devices
* [**Bugfix**] Fix bug when creating folder while multiple rows are selected 
* [**Bugfix**] Fix bug with empty menu in torrent client torrents tab when in mobile view 
* [**Bugfix**] Fix bug with rTorrent paths configuration and spaces that caused daemon to crash 
* [**Bugfix**] Fix bug when adding FTP connections with invalid hostname and infinite loading 
* [**Bugfix**] Fix bug with wrong disk space indication in bottom bar 

### **Version 1.7.4 (12/Sep/2018)**

* [**Feature**] Implement torrent client configuration
* [**Feature**] Implement torrent client bottom bar with misc global controls and statistics
* [**Feature**] Implement speed limiter per torrent (Deluge only at the moment)
* [**Feature**] Implement torrent client search
* [**Feature**] Implement the ability to download a .torrent file via the torrent client
* [**Feature**] Implement torrent client ratio color indication 
* [**Improvement**] Add 'Tracker Status' under torrent details 'General' tab
* [**Improvement**] Smoother UI and misc bug fixes for all devices

### **Version 1.6.8 (25/Jun/2018)**

* [**Bugfix**] Fix bug with torrent creation and infinite loader

### **Version 1.6.7 (18/Jun/2018)**

* [**Feature**] Implement 'Go to files' shortcut in torrent client right click menu
* [**Improvement**] Cleaner and more condensed torrent client list
* [**Bugfix**] Fix bug with 'Change Path' under torrent client with Deluge connections
* [**Bugfix**] Fix bug with torrent uploading and broken download location when torrent contained comment
* [**Bugfix**] Fix bug with 'Completed' filter under torrent client with rTorrent connections

### **Version 1.6.3 (24/May/2018)**

* [**Feature**] Implement torrent details drawer with General, Files, Trackers and Peers tabs:
  * **General:** Useful generic information about the torrent
  * **Files:** The torrent file list with information about the total progress of each file and current status. Also allows to set the priority and strategy  for a specific file on right click
  * **Trackers:** The trackers which the torrent is currently using
  * **Peers:** A list of peers which are currently connected
* [**Feature**] Implement ability to edit a torrent from within the torrent client
* [**Feature**] Improve torrent uploader and provide the ability to set directory and label during upload
* [**Feature**] Make dashboards remember their last location when they get re-mounted
* [**Feature**] Implement multi-selection in mobile file browser list
* [**Improvement**] Increase label width in torrent list for all devices 
* [**Improvement**] Remove bounce animation from mobile context menus
* [**Improvement**] Re-group torrent client context menu items
* [**Improvement**] Major performance boost when doing actions on multiple torrents
* [**Improvement**] Smoother UI and misc bug fixes for all devices
* [**Improvement**] Improve mobile main menu design
* [**Improvement**] Smoother UI and misc bug fixes for all devices
* [**Improvement**] Add home pathfor FTP/SFTP storage drives to the file browser breadcrumbs popup
* [**Bugfix**] Fix bug in mobile view when opening folder on row click
* [**Bugfix**] Torrent client Upload button should be disabled when there is no active conneciton
* [**Bugfix**] Fix favicon size proposions in trackers filter and use a default one when favicon is missing
* [**Other**] Misc security improvements
* [**Other**] Migrate all local default rTorrent XMLRPC connections to SCGI for improved performance

### **Version 1.5.0 (27/Feb/2018)**

* [**Feature**] Theme preference selection via profile settings. Currently implemented light and dark themes
* [**Feature**] Quickly upload files or torrents by drag and dropping to the browser
* [**Feature**] Ability to re-index local files from profile/drives
* [**Feature**] Change torrent save location from the right click menu in the Torrent Client
* [**Improvement**] Sort labels in torrent client filters alphabetically 
* [**Bugfix**] Disabled keyboard when trying to use HTML inputs while profile/dashboards is active
* [**Improvement**] Smoother UI and misc bug fixes

### **Version 1.4.3 (17/Jan/2018)**

* [**Bugfix**] Fix issue with downloading files via share link with unsupported filename encoding in HTTP headers

### **Version 1.4.2 (28/Dec/2017)**

* [**Bugfix**] Fix disk space validation issue with Google Drive 'unlimited' accounts

### **Version 1.4.1 (15/Dec/2017)**

* [**Bugfix**] Properly close unused SFTP connections

### **Version 1.4.0 (15/Dec/2017)**

* [**Feature**] Ability to create dashboards with FTP/SFTP storage drives
* [**Feature**] Ability to copy folders between storage drives
* [**Feature**] Ability to assign different colors to each label in the Torrent Client
* [**Feature**] Easily add torrents to the torrent client via the file browser right click menu
* [**Improvement**] Smoother UI and misc bug fixes
* [**Other**] Misc improvements with automatic syncing between the seedbox and seedbucket

### **Version 1.3.0 (10/Nov/2017)**

*  [**Feature**] Responsiveness for mobile, tablet devices and smaller screens in general
*  [**Feature**] Implement the ability to download from direct HTTP/HTTPS/FTP/FTPS links to any storage drive
*  [**Feature**] Implement the ability to set torrent priority via the context menu (for rTorrent connections only)
*  [**Feature**] Implement the ability to manage torrent labels via the context menu (Torrent Client)
*  [**Feature**] Allow selecting multiple files by holding the SHIFT key (File Browser)
*  [**Feature**] Allow sharing/unsharing multiple files simultaneously 
*  [**Improvement**] Reduced the number of columns shown in the torrent client and provided the ability to scroll them left or right by clicking on the header arrows or with the keyboard ARROW LEFT or ARROW RIGHT keys
*  [**Improvement**] Add disk space info indicator to the File Browser
*  [**Improvement**] Smoother UI and misc bug fixes
*  [**Other**] Disable full file indexing from running on every seedbox restart, making the File Browser unusable for a few minutes
*  [**Other**] Allow users with unsupported browsers to be able to use the web app on their own risk of not working properly

### **Version 1.2.4 (19/Sep/2017)**

*   [**Improvement**] Auto-select input text when renaming file in file browser

*   [**Improvement**] Hide "Add Dashboard" modal when "Add Storage" modal is visible

*   [**Improvement**] Show error message in torrent file uploader when the user tries to upload an invalid file type

*   [**Bugfix**] Disable "Copy" button in "Copy To" modal when the button is loading

*   [**Bugfix**] Fix overwrite when copying files in Google Drive and file already exists

### **Version 1.2.3 (18/Sep/2017)**

*   [**Improvement**] Better english text in file browser indexing loader gif

### **Version 1.2.2 (18/Sep/2017)**

*   [**Bugfix**] Fix positioning of "New transfers added!" popup message

### **Version 1.2.1 (18/Sep/2017)**

*   [**Improvement**] Get rid of loader flashing in file browser when list loads very fast
*   [**Improvement**] In "Copy To" modal make the folder list disabled when selecting new adapter instead of hiding it

*   [**Improvement**] Show loading gif image when files are being indexed in the file browser
*   [**Bugfix**] Fix buggy scroller in "Move To" and "Copy To" modals when content was overflowing

### **Version 1.2.0 (15/Sep/2017)**

*   [**Feature**] Ability to create dashboards and manage them via user profile
*   [**Feature**] Ability to connect cloud drive storages and manage their files. Currently supported:  

    *   Google Drive
    *   Dropbox
    *   OneDrive
*   [**Feature**] Add 'Added At' column in the torrent client
*   [**Feature**] Ability to copy files between any two drives or within the same drive
*   [**Feature**] Add 'Force Refresh' functionality on torrent client right click menu
*   [**Feature**] Add 'Update Trackers' functionality on torrent client right click menu
*   [**Feature**] Rename file on ENTER when single file is selected in file browser
*  [**Improvement**] Smoother UI and misc bug fixes
*   [**Improvement**] Add colorized bullets next to torrent name to easily identify current status
*   [**Improvement**] Show browser right click menu when right clicking a row in file browser while in edit mode
*   [**Bugfix**] Disable submit on feedback modal when user presses ENTER
*   [**Bugfix**] Incorrect forgot password link in forgot password email

### **Version 1.0.0 (13/Jul/2017)**

*   [**Feature**] File Browser with basic actions:
    *   Copy
    *   Rename
    *   Move
    *   Create Torrent
    *   Compress/Uncompress most formats
    *   Download
    *   Share Link
    *   Resumable Uploads
    *   Sortable files list
*   [**Feature**] Torrent Client which supports Deluge and rTorrent with basic actions:
    *   Start/Stop torrents
    *   Remove torrents with or without data
    *   Upload torrents
    *   Sortable torrents list
    *   Connection manager
    *   Torrents filtering
*   [**Feature**] Use Profile for updating e-mail and password