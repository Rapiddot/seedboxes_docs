---
id: how-to-extract-an-iso
title: How to extract an ISO
description: Learn how to extract an ISO file via SSH with simple steps. Follow our guide to easily extract ISO files on your server.
keywords:
    - extract ISO
    - ISO file extraction
    - SSH ISO extraction
    - server ISO extraction
---

# How to extract an iso
In order to extract an ISO you need to do it via SSH. Just follow these easy steps:

1. [Login to your account via SSH](./How_to_connect_via_SSH_to_your_account.md)

2. Go to the folder where your ISO is located by using the cd command (e.g.  ***cd files/downloads*** )   

3. Extract the ISO by using the following command:

```bash
7z x -y -oOUTPUT_ DIRECTORY YOUR_ ISO.iso
```

That's it! Your ISO should now be inside the output directory you've specified.

:::info
Have in mind that you can only extra data .isos in this way. Bluray or DVD Video isos, have a completely different format and require special apps written for this purpose in order to be extracted.
:::