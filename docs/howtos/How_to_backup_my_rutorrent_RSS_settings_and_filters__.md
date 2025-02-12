# How to backup my rutorrent RSS settings and filters

Rutorrent stores its rss settings and filter list in a single file, in json format, which - although rare - is easy to get corrupted over time.

We highly recommend that you **backup** your rss settings periodically, so that if anything happens, **you will be able to restore them to any rutorrent instance**.

In order to backup your settings, you need to connect via SFTP or SSH to your account, and keep a copy of the following folder if you use rutorrent3:

```~/.www/rutorrent/share/users/_username_/settings/rss/```

or this folder if you have rutorrent 4 or 5

```~/.apps/rutorrent4/rutorrent/users/_username_/settings/rss/```

You should replace _username_ and _servername_, with your account username and your server's name respectively.