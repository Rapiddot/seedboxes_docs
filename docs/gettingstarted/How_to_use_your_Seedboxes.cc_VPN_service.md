---
toc_min_heading_level: 2
toc_max_heading_level: 4
---

# How to use your Seedboxes.cc VPN Service

## Introduction

Our VPN service is solely based on the popular [Wireguard](http://www.wireguard.com) protocol. The decision to support only the Wireguard protocol, comes from the fact that it is the most actively maintained vpn protocol, supported on any single operating system, open source, extremely fast, and provides extremely good encryption for everyday usage without slowing down your speed. Furthermore Wireguard was developed with the mobile connected world in mind, providing roaming for mobile devices as well (switching from one internet connection to another, works seamlessly and flawlessly).

## Wireguard app

### Download/Install

Visit the official Wireguard site which you can find [here](https://www.wireguard.com/install/) .

For faster reference, the links to download the app are as following;
> [Windows](https://download.wireguard.com/windows-client/wireguard-installer.exe)
> 
> [MacOS (App Store)](https://itunes.apple.com/us/app/wireguard/id1451685025?ls=1&mt=12)
> 
> [Android (Play Store)](https://play.google.com/store/apps/details?id=com.wireguard.android)
> 
> [iOS (App Store)](https://itunes.apple.com/us/app/wireguard/id1441195209?ls=1&mt=8)
> 
> [Linux](https://www.wireguard.com/install/)

Proceed to installing the Wireguard app as you would normally do with any other app

!!!info Note
For Linux, depending on its distro, you might have to install some packages more. For instance, for Ubuntu, you need to also install resolvconf via "sudo apt install resolvconf".
!!!


### Create connection

You first need to generate a Wireguard connection. Don't worry, the process is simplified and automated for you!

Just visit your seedbox at your client area, click the tab **"VPN"** and then the **"+ Add VPN connection"** button

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648459423755.jpeg)

!!!info Note
Depending on your seedbox tier, you can generate up to a certain number of Wireguard configurations to be used simultaneously. For the Bat Box tier, that number is 2 whereas for the Red Dragon tier, that number is 5.
!!!

At the new modal, name the connection to your liking (e.g. macbook) and click the **"Create VPN Connection"** button

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648459527106.06.58.jpg)

That was it, the connection is generated. You can now download it via the **"Download Configuration"** button

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648459846806.jpeg)

### Setup

The  configuration (tunnel) is now ready to be used. For desktops/laptops, you download the configuration file. For tablet/mobile devices, you scan the QR Code instead.

#### Windows / OSX

At the new modal, you can choose the country of the VPN server. For best performance, it is already preselected for you

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648460150844.34.34.jpg)

Alternatively, click to reveal the dropdown menu and manually select a) the country of the VPN server and b) the VPN server itself

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648460231246.09.15.jpg)

Either way, click the **"Download Wireguard VPN Configuration"** once ready so you can download the file locally.
The filename should be something like **"sbccvpn_wireguard.conf"**.

Open up your Wireguard app and choose to import the file you just downloaded. You should see a button named **Import tunnel(s) from file** or equivalent.

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648460775037.jpeg)

Select that file and proceed. That's it! You have successfully set up the Wireguard connection.
To use it, just click the Wireguard icon at the taskbar and select the "sbccvpn_wireguard" option to connect to the VPN server

#### Old OSX version

Since there is no GUI support for wireguard for older version of OSX ( < 10.14), you must run it via the command line (terminal). But firstly, you need to install **homebrew** utility on your Mac: [https://brew.sh](https://brew.sh)

Just copy the command on the front page, paste it in your command line window and run it.

Once it's installed you can continue by installing the necessary packages for wireguard by running the commands:

```bash
brew install wireguard-go
brew install wireguard-tools
```

Next step is to rename the wireguard conf file you downloaded in the previous steps in order to remove the underscore (as it doesn't want any special characters). For example: "sbccvpn_wireguard.conf" has to be renamed to **"sbcc.conf"** (or anything you want without special characters, as said, and it should end with **.conf** extension) and save it to a safe location. Lets say that you saved it in your **Documents** folder inside your home path.

Final step is to run the command by providing the **full path**

```bash
wg-quick up ~/Documents/sbcc.conf
```

It will ask you for your user's password. Once you provide the password, you should now be connected to the VPN. Try launching a browser and see it your IP changes by going to [https://www.iplocation.net/](https://www.iplocation.net/) (or any website that shows your ip)

To disconnect run the command:

```bash
wg-quick down ~/Documents/sbcc.conf
```

#### Linux

As with older version of OSX, there is no available wireguard GUI for linux, so you must proceed according to your distro's guides or forums.
For example, for Ubuntu, after you have successfully installed wireguard (and resolvconf, as stated above) via "sudo apt install wireguard resolvconf", you need to rename the wireguard conf file to **wg0.conf** and copy it to **/etc/wireguard/** while using sudo for the cp action.
In order to activate the connection, you need to do the following;

```bash
sudo wg-quick up wg0
```

To disconnect run the command:

```bash
sudo wg-quick down wg0
```

#### Tablet / Mobile

For tablet/mobile devices, you again select the VPN country and server as with Desktop / Laptops (or just use the preselected / default), but now you click the **"Get Wireguard QRCode"** button instead.
**Note:**: You could download the configuration file to your device and then import it (as you would do with desktop / laptop) but the QR code is easier and faster.

A new modal will appear with the QR code revealed

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648461338777.09.59.jpg)

!!!info Note
The above QR code is invalid, it is only shown as a demonstration
!!!

Open the wireguard app from your tablet or mobile device and either click the **"+"** icon at the top right of your screen or click the **"Add a tunnel"** button

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648462904700.21.22.jpg)

At the dropdown menu, click the **"Create from QR code"** link

![](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1648462913397.21.34.jpg)

This will open your camera (make sure that you have given permissions for allowing the camera to be used) so you can scan the QR Code.
You can name the tunnel to your liking (e.g. sbccvpn). After that, you need to allow it so your tablet /mobile can use the VPN connection you just set up.

**NOTE:** Try to rename the config file to something that **does not contain spaces and special characters** (like "sbcc" as previously written) or the server location like "France" before importing it, as there is currently a bug with Wireguard and Android mobiles.

That was it, you can now easily enable it and connect to the VPN server at your convenience!

## Additional considerations about the service

A wireguard connection created in your client area can be installed in many devices if you wish, but only one of them can be connected simultaneously. This is a limitation of the way Wireguard works. If you try to connect at the same time from a second device with the same connection, it will either fail or your previous connected device will log out automatically.

If you need 2 simultaneous connections, create a second connection from your client area, and download a second configuration to your second device. All our plans include at the minimum 2 connections and depending on your plan, up to 5.

If you choose the option "Auto" in the country selection when you download your configuration, what happens is, that everytime you try to connect, you will be connected to a server as near as possible to your current location. If you are in Germany you will be connected to a German server, and if you are in France, you will be connected to a French server. This will result in the best speed possible as well while anonymizing all your traffic.

You can download the same configuration of the same connection multiple times, with different countries selected, and install all of these configurations in your devices. Then you can simply connect each time to the country you want. However, remember, you can only be connected at the same time with one device while using the same connection.