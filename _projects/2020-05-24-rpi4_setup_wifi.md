---
title: "Set up Raspberry Pi 4(Wi-Fi)"
date: 2020-05-24T01:59:33+05:30
author: Karhtik Mahendra
avatar: /me.png
authorlink: https://ikarthikmb.github.io
cover: /posts/rpi_ethernet/rpi_thumb02_square.jpg
categories:
  - posts
tags:
  - raspberry pi
  - wifi
  - howto
nolastmod: true
draft: false
---

![](/posts/rpi_ethernet/rpi_thumb02.jpg)

**Contents**


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=true} -->

<!-- code_chunk_output -->

- [Hardware Requirements:](#hardware-requirements)
- [Steps to install the required software tools](#steps-to-install-the-required-software-tools)
  - [Further Steps:](#further-steps)
- [Accessing Pi Desktop Remotely](#accessing-pi-desktop-remotely)

<!-- /code_chunk_output -->

---

The set up for Raspberry Pi using Wi-Fi is the same as the previous article on how to Set Up Raspberry Pi 4 through laptop/pc using Ethernet cable(No Moniter, No Wi-Fi) with some minor changes which we are going to see. 

## Hardware Requirements:

1. Raspberry Pi 4 Model B (1/2/4 GB RAM)     
2. USB Type-C power supply         
3. Personal computer

## Steps to install the required software tools

1. If you had followed the previous article then skip these steps and move to 'step-6'. From the official raspberrypi.org download the Raspbian Buster operating system[^1]

[^1]: [Raspberry pi official website](https://www.raspberrypi.org/software/operating-systems/)

2. Also, download the Raspberry Pi Imager from the website[^2], this is for writing the image file onto the SD card.

[^2]: [Raspberry pi imager download](https://www.raspberrypi.org/software/)

3. If you are using windows you probably have to download the ssh client, I prefer downloading it from Bitvise ssh client from PuTTY.

### Further Steps:

4. To access the desktop of the pi, you can either connect a micro to HDMI connector from the pi to a monitor or you can access it remotely on your PC/laptop. To connect remotely VNC-server has to be installed onto the pi by default the VNC-server is installed within the operating system, in order to view it remotely one has to download VNC-viewer on his/her Desktop.

5. Open the Raspberry Pi Imager and select the custom setup then select the OS from the Downloaded folder and carefully set the target as a USB drive. Wait for the image to be written on the card.

6. After done, open the boot folder, create a new document named **“ssh”** without any extensions. Create another text file, enter the following configurations and save it as `wpa_supplicant.conf`. Dont forget to enter the country code and the wi-fi credentials. 

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=<Insert country code here>

network={

    ssid="testing"
    psk="testingPassword"

}
```

7. Now power up the pi with the type-C cable and wait for a while for the pi to be connect to your Wi-Fi.

8. Open Advanced IP Scanner and make a quick scan, identify the Raspberry Pi and note the IP address.

9. Open the Bitvise SSH Client[^3], enter `raspberrypi.local` or the IP address(from the previous step) as host and leave 22 as default port in the server section.

[^3]: [Bitvise SSH Client](https://putty.org/)

10. Click Log in and enter the username as pi and the default password as **raspberry**. A terminal pops up and you are now into the Raspberry Pi.

11. If this is your first time logging into pi make sure to update your pi by issuing the command `sudo apt-get update` and then `sudo apt-get upgrade` to upgrade. 

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

> **Quick tip:** Don’t forget to change your password once you are logged in.

## Accessing Pi Desktop Remotely

12. Go to *terminal* and type `vncserver`, notedown the generated **ip address**. Now open *VNC-Viewer*[^4] on your desktop and enter the **ip address** or paste it, after few seconds a window pops sharing the screen of raspberry pi desktop. 

[^4]: [real-vnc-viewer official website](https://www.realvnc.com/en/connect/download/viewer/)

