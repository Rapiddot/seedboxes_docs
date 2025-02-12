# Setup Rclone on 2 Machine Setup

**Credits:** to **angoikon** with his reply to a question [here](https://community.seedboxes.cc/questions/rclone-crypt-mounted-drive-on-local-pc), who told us how to do it. I just wanted to expand it so other users that are still kind of new to all of this, understand how to do it. It honestly is easy once you understand how it works. Basically we setup a connection to our G Drive via Rclone, Mount it as a local drive and use the Encryption Keys to decrypt it for PMS (Plex Media Server) to read.

**Overview**
Setting up the Encrypted Google Drive is easy, which works if we want to use the seed box for downloading and streaming the media. But for users, like myself, we want to setup the PMS (Plex Media Server) on a local machine or a remote machine to stream the media. I am based in the USA and it's not easy finding a seed box locally, so this is why I am doing this setup. 

1. Setup rclone on your Seed Box via [this guide.](https://community.seedboxes.cc/articles/how-to-mount-a-remote-drive-to-your-seedbox) **I would make sure to make to grab a copy of your Client ID and Client Secret for Step 3**
2. Once you got that setup, you will want to install rclone on your second box.
3. Connect rclone to your existing drive you setup in Step 1. You can use [this guide](https://rclone.org/drive/) as a reference. 
 * However, instead of leaving your Client ID and Client Secret blank, you would fill these in as you use the guide. You would get these from the initial setup. (If you didn't grab them, you can [go here](https://console.developers.google.com/) to find them. They are under the "Credentials" Tab on the left > "OAuth 2.0 Client IDs"
 * You can stop using the guide at the "rclone lsd remote:" part.

This is the rclone config file for my drive: (Yours may vary depending on the name you gave it)

```
[gdrive]
 type = drive
 scope = drive
 token = {"access_token":"**Encrypted**"}
root_folder_id = **Encrypted**
```

4. Now, go to your seedbucket, find the encrypted folder, right click it and select "Encryption details".
  * Note: If you did whole drive encryption, go to your settings -> Drives and select "Encryption details" at the drive. You could also see the encryption folder details from here, just click "Show keys" for the corresponding encrypted folder.
Either way, at the new window click the "Rclone settings" and press the "Copy to clipboard" button.
5. Go back to your Local or Remote PC, edit the configuration file with your favourite terminal editor and Paste the clipboard at the bottom of the file.
	* Linux: "~/.config/rclone/rclone.conf"
	* Windows: "C:\Users\USERNAME\.config\rclone" 
6. You will need to do two changes;
 * Rename the "[CRYPT NAME]" to something distinguishable e.g. [gcrypt] (without quotes, only the brackets and the name of the mount), and
 * Rename the "remote = YOUR REMOTE:/FOLDER" with the name you gave your Google drive (e.g. gdrive, see above), so it should be written as "remote = gdrive:/FOLDER" (replace FOLDER with encrypted folder filename or if you set encryption to a folder or "remote = gdrive:" if you set whole drive encryption). Again, without the quotes.
7. Save and exit.

Example of  How my rclone config file looks:

```
[gdrive]
 type = drive
 scope = drive
 token = {"access_token":"**Encrypted**"}
root_folder_id = **Encrypted**

[gcrypt]
type = crypt
remote = gdrive: (Take Note that the remote is the same as the name in the brackets [ ])
filename_encryption = standard
directory_name_encryption = true
password = **Encrypted**
password2 = **Encrypted**```

*Make sure the "remote =" is the name as the drive we setup earlier with the Client ID and Client Secret. So for example, mine is called [gdrive] so I put "remote = gdrive:" under the [gcrypt].*

8. Finally, follow the procedure here to mount the remote as file system on a pre-created empty mountpoint of your choice, so something like:

 * Linux: rclone mount gcrypt: ~/mount
 * Windows: rclone mount gcrypt: z:

There is a bunch of [different parameters](https://rclone.org/commands/rclone_mount/) you can add instead of using just rclone mount gcrypt: z:. 

**Don't forget to add the new library paths and re-scan your content, so you can stream from your local server.**