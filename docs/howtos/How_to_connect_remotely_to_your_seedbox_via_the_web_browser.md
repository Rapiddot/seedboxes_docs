---
id: how-to-connect-remotely-to-your-seedbox-via-the-web-browser
title: How to Connect Remotely to Your Seedbox via the Web Browser
description: Learn how to easily connect remotely to your seedbox using your web browser without the need for extra applications or terminals.
keywords:
    - seedbox
    - remote connection
    - web browser
    - SSH
    - seedbucket
    - SFTP
    - FTP
    - terminal
---

# How to connect remotely to your seedbox via the web browser

## Introduction

There are several ways to connect to your seedbox, like [FTP](https://community.seedboxes.cc/articles/how-to-connect-via-ftp-to-your-account-using-filezilla), SFTP, [SSH](https://community.seedboxes.cc/articles/how-to-connect-via-ssh-to-your-account) or via our own app, [seedbucket](https://community.seedboxes.cc/articles/how-to-use-seedbucket). 

**Note:** If you want to see hidden files and folders, then SFTP (with the use of an SFTP client) or SSH (via a terminal console) are the only ways to do so.

We have now implemented another, very easy way to connect remotely to your seedbox, by using your favourite browser - no extra applications or terminals or remembering ports etc. It is essentially a remote SSH session, so you can see hidden files and folders too

## Browser

Open up your favourite browser and navigate to [https://remote.seedboxes.cc/](https://remote.seedboxes.cc/)  .
For username, use your **client area email address** and input your client password at the corresponding field

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1615370363789.png)

### Open sessions
At the new page, you can see at the top your most recent connections and all of your available connections / seedboxes.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1615371051944.png)

:::note
At the screenshot, the user has two seedboxes so both appear at the list.
:::

Just click the seedbox you wish to open a session for and it will automatically do so - no need for inputting your seedbox username/password!
A terminal console within the browser will appear and you will be ready to use your SSH session.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1615372158763.png)

### End session

After you have finished, type **logout** and press enter, or just close the browser's tab.

That was it!

### "Screen" - advanced usage

If you need to perform a command via your terminal that is a bit time-consuming and you need to e.g. close your PC or your browser, this will mean that you will be also ending the session thus terminating the command.
In that case, you could always use the **screen** terminal app which is already pre-installed to your seedbox.

Once you connect remotely via the above steps to your seedbox, type **screen** and press enter twice.
It will create a virtual screen within your shell, so you can run afterwards the command, in screen mode.
The advantage of screen is that you can close the terminal window or just detach the screen (with **ctrl + a + d** ) or even close the browser/tab, and the process won't be terminated (it will run at "background").

To return at any time to that virtual screen, connect remotely once more and once you are logged in, type **screen -ls** and hit the enter button. Check the first digits of that session, then type "screen -r DIGITS" (e.g. **screen -r 34295**) to reattach that screen to current terminal and continue from where you left off.
