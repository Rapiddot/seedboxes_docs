# How to setup your media server through Cloudflare proxy

## Introduction
If you experience buffering when you try to stream from your seedbox media server or the server keeps transcoding to lower resolutions due to network latency, and [rerouting traffic via another carrier](./How_to_reroute_traffic_through_another_carrier_towards_your_IP_by_using_our_speedtest_and_reroute_tool.md) doesn't solve your network issues, we are now introducing you to Cloudflare's CDN via a custom domain name (aka proxy).

This way, your ISP won't have to go to many different networks to reach our own - and finally your seedbox.

:::note
You need to get a custom domain name (paid) as well as a Cloudflare account (free).
Also, don't forget to send us a ticket from your client area with the domain name so we can configure your media player properly** 
:::

## Create accounts
### Domain name
There are many sites that you can buy a domain name like namecheap.com or godaddy.com . If you Google it, you will find many more.
The cost for such a domain name is almost insignificant (a couple of dollars/euros per year) and its advantages can be huge, as you will see later on.
For this guide, we will be using namecheap.com . So create an account there and purchase the domain name of your choice. You might have to be a bit creative in order to find a custom name that it is not already taken. But don't worry, it can be anything you want (and have any extension!).

Once you purchase a custom domain name (e.g. mysite.club), head to cloudflare.com

### Cloudflare
Create an account at cloudflare too.

Once it is ready, at the main screen of cloudflare dashboard, press the **+ Add Site** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649410564329.14.33.jpg)

At the next page, input your custom domain name (e.g. mysite.club) you just bought and press the **Add site**

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649410611266.15.29.jpg)

You will be greeted with a billing option for your custom domain. Just click the **Free**  option and then click the **Continue** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649415679369.16.37.jpg)

You will be given the following directions; You will need to remove the nameservers and replace them with the ones that cloudflare gives you

**Note:** You might get other nameservers that the ones shown at screenshot, this is to be expected

## Make changes
### Change nameservers
Head back to namecheap.com (or the site you purchased the domain from) and go to your account.

At the left side of your screen, click the **Domain List** under your Dashboard. Search for the **NAMESERVERS** tag and change the dropdown menu to **Custom DNS** . You need to paste both links from the previous step that cloudflare provided you with

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649668302349.08.45.jpg)

**Note** You will see an informational message that the change you just did might take up to 48 hours in order to be detected. You might though get an email in an hour, you probably won't have to wait that long

### Add DNS entry
Once you receive the email , head back to cloudflare.com and click the **DNS** tag at the left section of the screen.

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649412568358.02.39.jpg)

At the center of the screen, you can see the DNS management for your site. Just click the **+ Add record** button so you can add a new DNS entry

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649412673976.05.18.jpg)

You need to know two things before you proceed with inputting the record. The first one is your **seedbox username** (easy!) and the second one the **IP** of your seedbox server.
For the latter, leave the cloudflare tab open and open a new tab in your browser. Head to your client area at **seedboxes.cc** and click your seedbox in which your media server resides (let's assume that you are using **plex** as your media server).
Under the seedbox information, you can see the **Server IP**, so just copy that and be ready to paste it at cloudflare

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649414842269.20.28.jpg)

> Type: A,
Name: **seedboxusername**-**plex**
IP: **185.149.90.100**

Go back to the cloudflare tab and input the above in bold with the correct ones (your seedbox username, the type of media server you use - which should be either one of plex, emby or jellyfin - and the server IP for that media server). Yours will of course differ from the ones shown

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649415076772.45.20.jpg)

Click the **Save** button and the proxy should have been enabled.

Also, check that the SSL/TLS is set to **Full** encryption. Just click the equivalent link at the left section of the screen and make sure that it is enabled

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1649415498634.png)


### Add page rule

Finally, you will have to create a page rule for your plex hostname to disable a few features which brakes Plex streams.
Just go back to your cloudflare dashboard, click the **Rules** tag at the left section of the screen, then the **Page rules** button and finally the **Create Page Rule** button

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1660290698798.43.10.jpg)

Create a Page Rule with the following options:

> **seedboxusername**-plex.**mysite.club**/*

(replace both bold with your username and domain name retrospectively) and set the following:

> Rocket Loader: Off
Cache Level: Bypass
Automatic HTTPS Rewrites: On

![file](https://rapiddot-support-community-uploads.s3.amazonaws.com/uploads/image-1660290889827.54.27.jpg)

Click the **Save and deploy page rule** button.

**Once you are done just send us a ticket with the domain name and we will configure everything on your Plex server to use the custom domain**