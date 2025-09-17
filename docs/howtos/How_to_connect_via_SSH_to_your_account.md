---
id: how-to-connect-via-ssh
title: How to connect via SSH to your account
description: Learn how to connect to your seedbox account via SSH using PuTTY on Windows or Terminal on Mac and Linux.
keywords:
    - SSH
    - seedbox
    - PuTTY
    - Terminal
    - Windows
    - Mac
    - Linux
---

# How to connect via SSH to your account
:::info
This is a guide on how to connect via SSH to your account directly from your pc. You can also do this from your browser by following this ![guide](../howtos/How_to_connect_remotely_to_your_seedbox_via_the_web_browser.md)
:::

## Windows Users
### SSH to your account with Putty
1. Download PuTTY from [here](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)
1. Install PuTTY.
1. Run PuTTY which should be found in your Start menu.
1. In the hostname field, enter your server hostname (ex. user.cloud.seedboxes.cc). You can find your server hostname in your activation email or in your service details in your client area.
1. In the port field, use the SSH port listed in your account details
1. Click Open

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491671331505.png)

1. You will be asked for your username. Enter your seedbox username.
1. Then you will be asked for your password. Enter your seedbox password. Please note that when you enter the password, you will see nothing being typed. This is normal and it is a security precaution.
1. If you entered your details correctly, you will be greeted with a welcome message and your account shell ready to accept any commands.

## Mac or Linux Users
### SSH to your account with Terminal
Openssh is builtin in Linux and Mac operating systems, so all you have to do in order to ssh to your account is

1. Open the Terminal application in your operating system
1. Type the command (substitute the username, SSH_PORT, with your account username and your account's ssh port that you can see in your seedbox details in your client area) : 

    ```
		ssh username@username.cloud.seedboxes.cc -p SSH_PORT
		```


1. You will be asked for your password. Enter your seedbox password. Please note that when you enter the password, you will see nothing being typed. This is normal and it is a security precaution.
1. If you entered your details correctly, you will be greeted with a welcome message and your account shell ready to accept any commands.

