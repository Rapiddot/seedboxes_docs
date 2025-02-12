Choose a guide depending on your operating system

## MAC OSX / Linux

Simply open a terminal and type:
```
ssh -l \{USERNAME\} -p {SSH_PORT} -D 6666 \{USERNAME\}.cloud.seedboxes.cc
```

It will ask for your password, you type the password and click enter. Once you login, minimize the window, but don't close it. 

Now, open your browser, and in your browser connections details, use a socks5 proxy with the following details:

* **hostname:** localhost
* **port:** 6666

 As long as the terminal is open, you will be connected to your seedbox.
 
 A more detailed section for Firefox is below, just scroll to the bottom

## MAC OSX
Alternatively and only for OS X, you can use the [SSH Tunnel Manager](https://www.tynsoe.org/v2/stm/) , which has a GUI.

## Windows

First you will need to download the bitvise ssh client. You can find it [here](https://www.bitvise.com/ssh-client-download). Install and run it.

1) On the Login Tab of the connection settings, type the settings as illustrated in the screenshot below. Substitute the blurred letters with your seedbox username (so host is **username**.cloud.seedboxes.cc and port is 3232). Use password authentication and save the password (so you don't mess with public keys in case you authenticate with keys)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1677222177145.png)

2) Then on the "Services" Tab, enable the socks server as illustrated in the screenshot. Choose a port e.g. 6666

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1677224281535.png)

Same as in MAC OS X/ Linux, open your Firefox browser, and in your browser connections details, use a socks5 proxy with the following details:

* **hostname:** localhost
* **port:** \{PORT NUMBER YOU CHOSE in step 2, 6666 in this case\}

Tip: You can make multiple profiles, one for each of your browsers (in case you use it in a more advanced way), just make sure to use a different socks proxy port for each connection.
This app is nice, works reliably, minimizes to your tray, has tons of options for automatic reconnects etc.

You can check a more detailed section for Firefox just below

## Firefox

Simply open your Settings and scroll down to the bottom so you can find the Network settings. Click the **Settings** button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1677222755949.png)

You can setup your SOCKS5 proxy and port from Manual proxy configuration. Use the same ports you selected at the previous steps (e.g. 6666)

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1677222780751.png)
