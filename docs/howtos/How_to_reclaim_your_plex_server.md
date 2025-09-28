---
id: how-to-reclaim-your-plex-server
title: How to Reclaim Your Plex Server
description: Learn how to reclaim your Plex server without reinstalling the Plex app and losing your library paths. Follow these simple steps to regain access to your Plex server on your seedbox.
keywords:
    - plex server
    - reclaim plex server
    - seedbox
    - plex.tv account
    - plex claim code
    - seedboxes
    - SSH
---

# How to reclaim your plex server

If for whatever reason your plex server is signed out of your plex.tv account and you no longer have access to your plex server, instead of re-installing the plex app (**which most probably will cause you to lose your previous library paths and a full rescan will be needed once you re-add them, amongst other things**), there is another, better and faster way (and without the above fuss in parenthesis). You just need to do the following in order to claim your plex server back:

## Option A - Use our Discord channel's Bot

The easiest way would be to do it from within our Discord Channel. If you are not already using our Discord channel, you can find instructions on how to connect to our Discord Channel and link your Discord account with your Seedboxes.cc account [here](../gettingstarted/Getting_started_with_Discord.md).

One you are in our discord channel, just use the following command to reclaim your plex server:

`/seedbox reclaim_plex <username> <plex_claim_code>`

where `<username>` is your seedbox username

:::info
You can get a new claim code, from the plex.tv website here -> [https://www.plex.tv/claim/](https://www.plex.tv/claim/)
:::

## Option B - Use the SSH access of your seedbox

1) Connect to your seedbox via SSH.
You can also easily do so from your web browser too, without the need to remember ports etc. Just visit [https://remote.seedboxes.cc/](https://remote.seedboxes.cc/) from your favourite browser and enter your **client area email** and **password** (like you do with seedbucket).

You can also check our guide for that [here](../howtos/How_to_connect_remotely_to_your_seedbox_via_the_web_browser.md)

Once you input your credentials, select the seedbox from the list (if you have multiple seedboxes) that you wish to reclaim the plex server. You will automatically connect via SSH to that seedbox and the terminal will appear

2) Without leaving that tab, open another tab, navigate to [https://www.plex.tv/claim/](https://www.plex.tv/claim/) and copy the new claim code for your plex

3) Return to your previous tab (with the terminal), and run the following two separate commands;

```bash
wget https://raw.githubusercontent.com/Rapiddot/tools/master/plex/reclaim.sh
bash reclaim.sh
```
 
4) You will be prompted for your claim code. Unfortunately some browsers doesn't support pasting from clipboard (via right-clicking), so you have to input the code manually. If you connected via SSH though (and not via your browser), you can directly paste it as usual

5) Go to your seedbox client area, in the seedbox details page, and then click on the "Installable apps" tab. Next to the Plex app, there is a "Restart" button, which restarts your plex server. Please restart your plex server. Then your plex server should be back online in a minute.

That was it!


:::note
In case you proceeded with plex re-installation prior to seeing this tutorial, as said there is no point in reclaiming as you now have a brand new plex server. You'll just have to re-add your libraries, both for your seedbox and for your mount. 
:::