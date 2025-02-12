## Seedboxes.cc VPN App

To use our VPN service simply download the Seedboxes VPN app, available for Linux. It is the simplest and most elegant way to be able to switch among different servers and countries, just with a click of a button.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491813908884.png)

In order to download our VPN client, please use the following links, depending on your system:

* [Download for Ubuntu Linux 32 bit (x86)](https://www.seedboxes.cc/download/vpn/ubuntux86)
* [Download for Ubuntu Linux 64 bit (x64)](https://www.seedboxes.cc/download/vpn/ubuntux64)

OpenVPN

An additional way to user our VPN service is with OpenVPN. 

* Download OpenVPN by opening a terminal and executing "sudo apt-get install openvpn".
* Log in to your account, select a seedbox and navigate to "Download VPN Configuration" under the VPN tab.
* Select a country and a server of your choice and download its OpenVPN configuration file(ending in .ovpn).
* In the local folder where the .ovpn file was downloaded, open a terminal and type "sudo openvpn [fileName]" where fileName is the name of the configuration file.
* OpenVPN should ask you for your seedbox username and password before successfully connecting.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491813914661.jpg)

After entering your username and password a connection to the server should be established within a few seconds.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1491813921266.jpg)