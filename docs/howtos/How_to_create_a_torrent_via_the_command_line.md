# How to create a torrent from the command line

1. First of all, you should start with [How to connect via ssh to your account](./How_to_connect_via_SSH_to_your_account.md)

2. After you connect to your slot via SSH, navigate to the directory which includes the folder that you want to create a torrent from, ex.

```bash
cd torrents/downloads/
```

3. Then you use the mktorrent command to create the torrent, as follows:

```bash 
mktorrent -v -a 'http://your_ announce_ url' -p DIRECTORY_ FOR_TORRENT
```

-v is for verbose -p is for private, as in not DTH or PeerExchange -a is for tracker url follows

for example:

```bash
mktorrent -a 'http://tracker.to/announce' -p Mozart_ Music_Collection
```

After mktorrent finishes, the torrent file will be saved on the same folder taking the name of the directory it was created for.

:::note
The command needs to be all in one line, and quotes must be used around the folder name if it contains spaces.
:::

If you want to specify piece size for torrent, you can use -l switch (small L) it's in potency of 2 so: 

2^19 = 524 288 = 512 KiB for filesizes between 512 MiB - 1024 MiB 
2^20 = 1 048 576 = 1024 KiB for filesizes between 1 GiB - 2 GiB 
2^21 = 2 097 152 = 2048 KiB for filesizes between 2 GiB - 4 GiB 
2^22 = 4 194 304 = 4096 KiB for filesizes between 4 GiB - 8 GiB 
2^23 = 8 388 608 = 8192 KiB for filesizes between 8 GiB - 16 GiB 
2^24 = 16 777 216 = 16384 KiB for filesizes between 16 GiB - 512 GiB This is the max you should ever have to use. 

2^25 = 33 554 432 = 32768 KiB (note that utorrent versions before 3.x CANNOT load torrents with this or higher piece-size)

Usage:

```bash
mktorrent -v -p -l 19 -a http://exampletracker.com/announce folder_name
```