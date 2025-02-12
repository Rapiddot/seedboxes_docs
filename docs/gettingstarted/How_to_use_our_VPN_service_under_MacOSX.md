You can use the Seedboxes.cc VPN service with your Mac operating system in 2 ways:

* By using our own MacOSX application
* By using the OS embedded vpn connection settings (using L2TP over IPSEC)
* By using Tunnelblick (OpenVPN protocol)

## By Using own own MacOSX application

The easiest way to use our VPN service, is to download the Seedboxes VPN app, available for MacOSX. It is the simplest and most elegant way to be able to switch among different servers and countries, just with a click of a button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491565262441.png)

In order to download our VPN client, please use the following link:

* [Download for MacOSX (10.8 and above)](https://www.seedboxes.cc/download/vpn/macosx)

## By using the OS embedded VPN connection settings

1. Navigate to "System Preferences" > "Network"

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491565334413.png)

2. Click on the plus ( + ) sign to add a new connection. Select **Interface**: VPN, **VPN Type**: Cisco IPSEC and give it a name. Then click "**Create**"

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1519461689662.40.51.png)

3. On the connection settings, type your seedbox's server hostname in the server address (ex. dracula.seedboxes.cc), your VPN username (usually the same as your seedbox username) in the Account Name and your VPN password in the password field. Then click the button "Authentication Settings"

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1519461901249.44.02.png)

In the Authentication Settings, use the Shared Secret: ***fastvpn***

   ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1519461936347.43.44.png)

Click OK. Then you should be able to connect by clicking the connect button.

## By using Tunnelblick with the openvpn protocol

1. Download [TunnelBlick](https://tunnelblick.net/) and install it in your Mac.

2. Download the VPN configuration file from within your [client area.](https://www.seedboxes.cc/client) We have instructions on how to do this [here](https://community.seedboxes.cc/articles/how-to-use-the-seedboxescc-vpn-service).

3. Right click on the "**seedboxescc.ovpn**" file you just downloaded, and right click on it, then select to open it with Tunnelblick

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491565744560.png)

4. You will be asked for Tunnelblick, if you want to install the configuration for All users on your mac, or only for your own user. Choose the option you want.

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491812076015.png)

5. You will then be asked for your administrator password, in order to complete the installation

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491812090658.jpg)

6. Once the installation finished, you will be able to connect. Upon the connection you will be asked, for your vpn username and password. You may choose to save these details to the "Keychain" so that tunnelblick will save them and not ask them again in the future.

    ![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491812102031.png)