# How to create and use rclone remotes in your seedbox

## Introduction

Rclone util is a command line program to (most commonly) move or copy files and directories from a source item (folder or file) to a destination folder.
It comes pre-installed with every seedbox.

Users might want this to utilize our fast network infrastructure in order to copy or move content **from their local seedbox towards a remote drive or vice versa** . The remote drive doesn't have to be a drive we currently support in seedbucket (Onedrive, Googledrive, Dropbox or any FTP/SFTP adapter), it can be anything you want - except 1Fichier or similar cloud drives that can't be installed in a headless machine. You can also perform those actions between different cloud drives.

:::note
You need to know how to SSH to your seedbox before proceeding - we have an excellent guide for that [here](./How_to_connect_via_SSH_to_your_account.md) . If you find SSH a bit challenging, you can easily connect remotely to your seedbox via a [web browser](./How_to_connect_remotely_to_your_seedbox_via_the_web_browser.md)
:::

## Remote installation

In this guide, we will be connecting a Google drive remote to your local seedbox. It can be either already connected to your seedbucket or not, it doesn't really matter. You need however to have pre-created the project along with the necessary credentials through your Google API [console](https://console.developers.google.com/). You can check out our rclone mount installation guide (for Google) [here](./How_to_mount_a_remote_drive_to_your_seedbox.md) for more information regarding the Google console and how to create projects, setting the OAuth screen and creating credentials.

:::note
The above link for the guide is describing the process for creating credentials (client id / secret) exclusively for seedbucket which is a web application. For plain rclone CLI usage, you need to create credentials with "Desktop app" application type (which obviously defers from the "Web application" application type. Using the same credentials but with the wrong application type will most definitely result in errors. Plus this wouldn't be good for your API's in the first place).
:::

We will use the default rclone configuration path which (will) reside in **/home/user/.config/rclone/rclone.conf** .

After you SSH to your seedbox terminal, follow the steps below

### Download latest rclone binary

Since Google has recently made a lot of changes to the authorization process (you might have received an email regarding the deprecation of OAuth out-of-band (OOB) flow), you now need to have at least the rclone version 1.58 installed. **This applies to both your seedbox and your PC**.

To check which version your seedbox uses, just issue the following command;

```rclone -V```

If you see at least 1.58 or greater, you can proceed to the next [step](#create-the-remote)

If not, you need to download the binary and place it at the correct path in order to use it. For that, you must do the following;

```bash
mkdir -p ~/.local/bin/
cd ~/.local/bin/
wget https://downloads.rclone.org/rclone-current-linux-amd64.zip
unzip rclone-current-linux-amd64.zip
mv rclone-\*-linux-amd64/rclone .
rm -rf rclone-*
echo $SHELL
```

The ~/.local/bin/ is already predefined for your local binaries, no need to set the path at $PATH .

:::note
At the time of writing this guide, the latest rclone version is 1.58.1 . You'll have to change the extracted folder name if you download another version, in order to move the binary file at the correct path.
:::

:::note
If you issue a "rclone -V" command and still see the old version, just logout and re-login to your seedbox via SSH
:::

### Create the remote

With the latest rclone version installed, you are ready to create the remote.

1) Issue the command

```rclone config```

This will initialize the terminal wizard which will guide you through the rest of the process

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656572894892.57.02.jpg)

2) Type **n** to create a new remote and press enter

3)  Give it a distinguishable name (e.g. **gdrive**)

4) From the list below, type the appropriate drive number and press enter. In our case, it is 17 as shown in the screenshot, however that depends in which rclone version is installed, yours might differ

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656572916139.58.15.jpg)

5) Open your [Google cloud console](https://console.cloud.google.com/) and navigate to your **project**, click at **Credentials** and then click at the **name** of the OAuth 2.0 Client ID. This will open up your id and secret

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1580898982259.png)

**NOTE**: You must have already created the project, given your consent through the OAuth consent screen, enabled the Drive API and created the credentials. Make sure those credentials refer to **"Desktop app"** application type, or else this won't work! **DO NOT USE THE CREDENTIALS YOU USED FOR MOUNTING YOUR RCLONE AT SEEDBUCKET AS YOU WON'T BE ABLE TO FINISH THE REMOTE POINT CREATION DUE TO ERRORS**. Don't forget that It is always best if you created a new set of credentials (with the correct application type in each case) in order to also minimize the API calls as they won't be shared between different apps

6) Copy and paste both **Client ID** and **Client secret** at the given fields

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656573037205.jpg)

7) Choose **1** to give rclone full access to the remote

8) At **root\_folder\_id** field, press **Enter** for using the default. This means that you will be at the root folder of your Google drive so you can see every single folder there.

9) At **service\_account\_file** field, press **Enter** for using the default

10) Choose to not **Edit advanced config** by pressing **n**

11) At the **Remote config**, choose **n** as your seedbox is a headless machine. An rclone command will be revealed which you need to copy to clipboard. As the output suggests, you need to paste that command in a machine with a web browser access. The fastest and easiest way is to open up a new tab at your terminal and paste it there.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656573208796.50.52.jpg)

:::note
It is best if you have also installed the same rclone version at your PC as in your seedbox (in this case, 1.58.1).
:::

The command should be something like that

```rclone authorize "drive" "someVeryLongRandomString"```

When you hit enter at your second tab at your terminal, another tab at your web browser will open so Google can automatically authorize. You can proceed to the next step.

:::note
Alternatively, in case you need to open it at a specific browser (and not your default one) you can append the following flag

```rclone authorize "drive" "someVeryLongRandomString" --auth-no-open-browser```
:::

This will reveal the link which you need to copy and paste it at the web browser of your choice (you should though be logged in with the same Google account as the one you created the credentials, in case you have multiple Google accounts). The link should be something like that;

```http://127.0.0.1:53682/auth?state=R-PBLFQ5Rgs1QvG5cBDhhv```

Of course, yours will differ. Once you are authorized, another string (config token) will be revealed at your second tab at your terminal. Just **copy** that and **paste** it at the **first** terminal (which is connected to your seedbox via SSH).

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656573237880.04.46.jpg)

12) Choose whether this drive will be configured as a team drive or not, and at the end, you will have created a preview of the remote drive. If everything is typed successfully, choose **y** and this will create the remote drive

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1656573179972.07.39.jpg)

13) You wil now see the newly-created drive with the distinguishable name you gave it (gdrive), just press **q** and enter to exit the wizard. Congratulations you have created your remote drive!

:::note
Depending on the drive, the above steps might differ, you can check the official rclone [site](https://rclone.org/) for information regarding a specific cloud drive.
The rest cloud drives should be a lot faster and easier to create, without the need to have web browser access
:::

### Rclone commands

You need to familiarize yourself with **lsd** (List all directories/containers/buckets in the path) and **ls** (List the objects in the path with size and path) rclone commands, so you know where you should move or copy content to.

For example:
```bash 
rclone lsd "gdrive:"
```

will list all directories under your "gdrive" remote. Notice the colon symbol "**:**" after gdrive. This is **mandatory**.

If you want to list all directories under a certain folder (e.g. "temp" folder that resides directly in your root folder), then you issue:
```bash
rclone lsd "gdrive:/temp"
```

and it will list all directories under (root) -> temp.

Same goes for **ls** command too.

:::note
You can issue the *"--max-depth 2"* flag at the end of each command to control the depth (default is 1). Also, we use double quotes ( **"** ) so there is no need for escaping characters.
:::

:::info Important
Linux is case-sensitive, which means that **temp** folder and **TEMP** folder are two different folders. You need to type the file/folder name exactly as you see it
:::


#### Rclone move

You will most probably needing to move content between your local seedbox and your remote drive (or vice versa).
However, before initiating a move, you need to set some flags in order for the move to be efficient.
At your terminal paste this:

```bash
ARGS=(-P --checkers 3 --log-file /home/user/.config/rclone/upload_rclone.log -v --tpslimit 3 --transfers 3 --drive-chunk-size 32M --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36" --delete-empty-src-dirs)
```

We are setting a progress bar along with the necessary log-to-be-created and a User Agent, that will be used in the rclone move command afterwards. Bear in mind that we have also set to delete empty source directories, after content is successfully moved to the destination drive. If however you want to keep the empty source directory, then remove the last flag.

:::warning
Each time you log to your terminal via SSH, you need to set that variable **ARGS** like above. Afterwards, you can initiate the rclone move (single or multiple times until you log out).
:::

**EXAMPLE**:
Lets say you want to move the contents of a folder that reside in "~/files/downloads/my pictures" at your local seedbox, towards your Googledrive "temp" folder. You need to issue the following:

```bash
rclone move "/home/user/files/downloads/my pictures" "gdrive:/temp" "$\{ARGS[@]\}"
```

This, however, won't move the folder "my pictures" itself, so if you want to move that folder too, you need to append it to your destination like this:

```bash
rclone move "/home/user/files/downloads/my pictures" "gdrive:/temp/my pictures" "$\{ARGS[@]\}"
```

:::note
You have to use double quotes everywhere as shown! This way, you don't have to escape characters.
:::

To check if the move was successful, you can do that with two ways: Either
```bash
rclone ls "gdrive:/temp"
``` 
or 
```bash
rclone ls "gdrive:/temp/my pictures"
```
if you moved the folder too, or

```bash
cat /home/user/.config/rclone/upload_rclone.log
```

to check the logs.

If you want to move content from your Google drive towards your local seedbox, the process is similar, just swap source with destination. So:

```bash
rclone move "gdrive:/temp" "/home/user/files/downloads/my pictures" "$\{ARGS[@]\}"
```

#### Rclone copy

Copy works similarly to move, but this time the arguments mustn't have the "--delete-empty-src-dirs" flag.
At your terminal paste this:

```bash
ARGS=(-P --checkers 3 --log-file /home/user/.config/rclone/upload_rclone.log -v --tpslimit 3 --transfers 3 --drive-chunk-size 32M --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
```

We are setting a progress bar along with the necessary log-to-be-created and a User Agent, that will be used in the rclone copy command afterwards.

:::warning
Each time you log to your terminal via SSH, you need to set that variable **ARGS** like above. Afterwards, you can initiate the rclone copy (single or multiple times until you log out).
:::

**EXAMPLE**:
Lets say you want to copy the contents of a folder that reside in "~/files/downloads/my pictures" at your local seedbox, towards your Googledrive "temp" folder. You need to issue the following:

```bash
rclone copy "/home/user/files/downloads/my pictures" "gdrive:/temp" "$\{ARGS[@]\}"
```

This, however, won't copy the folder "my pictures" itself, so if you want to copy that folder too, you need to append it to your destination like this:

```bash
rclone copy "/home/user/files/downloads/my pictures" "gdrive:/temp/my pictures" "$\{ARGS[@]\}"
```

:::note
You have to use double quotes everywhere as shown! This way, you don't have to escape characters.
:::

To check if the move was successful, you can do that with two ways: Either
```bash
rclone ls "gdrive:/temp"
``` 
or 
```bash
rclone ls "gdrive:/temp/my pictures"
```
if you moved the folder too, or

```bash
cat /home/user/.config/rclone/upload_rclone.log
```

If you want to copy content from your Google drive towards your local seedbox, the process is similar, just swap source with destination. So:

```bash 
rclone copy "gdrive:/temp" "/home/user/files/downloads/my pictures" "$\{ARGS[@]\}"
```

## Script / Cron job

So you successfully created your remote points and tested them with the command (e.g. move) of your choice.
You can of course automate this process so it runs -for example- twice per day, without the need for any manual interaction. This can be done by creating a script and creating the cron job for running that script. We can of course do that for you, just send us a support ticket, stating the remote points you created, which command to use (copy or move) and which source/destination folders are going to be used, and we will handle the rest.

:::note 
At the script creation below, you should use the **full path** of the binary file you downloaded, contrary to using directly the commands above.
:::

### Script creation
Using your favourite terminal editor (in this case, nano), create the script:

```bash
nano /home/user/.local/bin/offload.sh
```

Note: Make sure that the script resides inside your **/home/user/.local/bin/** - don't use custom paths. If you followed the above command, you are good to go.

Inside the terminal editor, paste the following:

```bash
LOCKFILE="/var/lock/`basename $0`"

ARGS=(-P --checkers 3 --log-file /home/user/.config/rclone/upload_rclone.log -v --tpslimit 3 --transfers 3 --drive-chunk-size 32M --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36" --delete-empty-src-dirs)

(
flock -x -w 5 200 || exit 1

/home/user/.local/bin/rclone move "/home/user/files/downloads/my pictures" "gdrive:/temp/my pictures" "${ARGS[@]}"

/home/user/.local/bin/rclone move "/home/user/other folder" "gdrive:/temp/other folder" "${ARGS[@]}"

) 200> ${LOCKFILE}
```

Of course you need to correct the paths, based on your needs. You can also add as many folders as you want (two are seen at the above example). Lastly, if you are going to use a copy action instead of move, don't forget to a) substitute **move** with **copy** for both commands and b) remove the **--delete-empty-src-dirs** at the end of the ARGS parameter as this flag is only valid for the move command.

:::note
You can also move/copy between different cloud drives, as long as you have created the remote points for both drives and you know the source/destination paths. For example, if you have created a dropbox remote point called "dbox" and you want to move content between certain folders, you could replace the above command with this one:
:::

```bash
/home/user/.local/bin/rclone move "dbox:/my pictures" "gdrive:/temp/my pictures" "${ARGS[@]}"
```

### Cron job
After finishing up with your script, it is best if you give it a go to see if you have set up everything correctly. To do so, you can manually run it:

```bash
bash /home/user/.local/bin/offload.sh
```

If it doesn't return an error, you can now create the cron job so that the script runs twice per day.

```bash
crontab -l | sed '/.*offload.sh.*/d' | \{ cat; echo "`shuf -i 0-59 -n 1` `shuf -i 8-11 -n 1`,`shuf -i 18-22 -n 1` * * * bash /home/user/.local/bin/offload.sh"; \} | crontab -
```

You should **really avoid** running the script more than two times per day (either via editing the cron so it is more frequent or manually running the bash command), as this might lead to API bans.

If you want to check the time (UTC) the script runs, just issue the command;
```bash
crontab -l
```

