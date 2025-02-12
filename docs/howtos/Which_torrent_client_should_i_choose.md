# Which torrent client should i choose?

We currently support all major torrent client for our slots. Below we will mention the pros and cons of each one:

## Qbitorrent
Currently our default torrent client, and one of the most popular ones, as it is supported in every operating system, it is actively maintained and offers all around the best performance with a nice native WebUI.


## Rtorrent (+rutorrent)
Rtorrent is a very popular client, however it is not that actively maintained as it used to be. Nonetheless it is a very stable and performant torrent client. One of its drawbacks is that it does not have a native WebUI and relies on rutorrent (a php implementation) to provide one. This adds complexity to the installation and has performance drawbacks when handling many torrents. Furthermore, rutorrent, while still actively maintained, has quite a few bugs.

## Deluge
Full featured and lightweight will cover all your needs, while it is very easy to learn for beginners. Beautiful native web gui, surely the most polished of all clients. Has better performance than rtorrent, although it cannot handle that many torrents efficiently as rtorrent. 

## Transmission
A nice, but not so lightweight client. Has less advanced features than all other clients, and does not perform that well either. However many users prefer it for its simplicity. Has a native WebUI, that is rather cumbersome if you want to handle many torrents.

:::info
In our seedboxes, you can only run one torrent client at any given time. This limitation is imposed for fair usage of our server resources among the users of the server.
:::

:::info
Have in mind that while some torrent clients offer the ability to autodownload from rssfeeds or irc channels (ex. autodl), you should not choose the torrent client based on that. The reason is that you can use Autobrr (available in your installable apps), an independent app which introduces rss and irc auto downloading functionality and can work with any of the above torrent clients and has a nicer webUI and many more capabilities. 
:::