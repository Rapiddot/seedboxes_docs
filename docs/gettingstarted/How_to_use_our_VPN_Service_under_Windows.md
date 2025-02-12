## By Using our own Windows application

The easiest way to use our VPN service, is to download the Seedboxes VPN app, available for Windows 7, 8 and 10. It is the simplest and most elegant way to be able to switch among different servers and countries, just with a click of a button.

In order to download our VPN client, please use the following links:

* [Download for Windows (7,8,10) 32bit (x86)](https://www.seedboxes.cc/download/vpn/winx86)
* [Download for Windows (7,8,10) 64bit (x64)](https://www.seedboxes.cc/download/vpn/winx64)

## With the build-in VPN client

**For Windows 10 only:**

1. Go to **Control Panel > Network and Internet > VPN**.
2. Click **"Add a VPN Connection"**.
3. Fill in your info, as shown in the image below. Substitute the "servername" with the name of your server, and use the username/password of your vpn user. Note that you will have to choose **L2TP/IPsec with pre-shared key** as the VPN connection type. For the Pre-shared key, type **fastvpn** . Scroll to the bottom and input your VPN **username** and **password**
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1591707281159.png)
4. Click "Save". Then you can connect to your VPN.

5. You can also use your VPN connections from your tray bar as well. Just click on the **"Network"** tray icon and from the network sidebar that will appear click on your VPN connection and **"Connect"**.

**For Windows 7 and above:**

1. Go to your Control Panel > Network and Internet > View Network Status and Tasks.
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492675877164.png)
2. Set up a new connection or network.

3. Connect to a Workplace.

4. Use My Internet Connection (VPN)

5. Use the following settings:
Internet Address: {YOUR_SERVER}.cloud.seedboxes.cc (we will use the banshee server for this example).
Destination name: Whatever you want (SBCC for this example). Make sure you check "Don't connect now; just set it up so you can connect later".
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492675915057.59.37_AM.png)
6. Go again to Control Panel > View Network Status and Tasks > Change Adapter Settings (it's on the left side).
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492677427277.png)
7. There should be a VPN adapter which you just created. Right click on it > Properties.

8. Go to the Security tab and select "LT2P/IPSec" for Type of VPN.
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492675929804.00.43_AM.png)
9. Underneath, that there is a button "Advanced Settings". Click that and select "Use preshared key for authentication" and enter "fastvpn" for the key (without the quotes).
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492675938993.01.00_AM.png)
10. Click OK and you are all set. Just double click the connection and it should connect.
![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492677466004.02.37_AM.png)
## With the OpenVPN client

1. Download the OpenVPN client.

2. Run the OpenVPN client.

3. Download the VPN configuration file from within your client area. We have instructions on how to do this here.

4. Copy the **"seedboxescc.ovpn"** file to the "config" folder which is located inside the installation directory of the OpenVPN client. If you did not change the default location during the installation it should be **"C:\Program Files\OpenVPN\config"**.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1492673548381.png)

5. The OpenVPN client will automatically detect and load the configuration file and you should be able to connect by right clicking on the OpenVPN tray icon located at the bottom right of your screen and then by clicking "Connect". If the configuration file is not at the correct location as mentioned above, no **"Connect"** option will appear.

6. You will be prompt for your VPN username (this will probably be your seedbox username) and password. Enter them and click **"OK"**. 

After a succesfull connection, the OpenVPN tray icon **will turn green** and you will be able to browse the internet anonymously!