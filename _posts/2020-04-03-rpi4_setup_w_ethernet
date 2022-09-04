---
title: Set Up Raspberry Pi 4 through laptop/pc using Ethernet cable(No Monitor, No Wi-Fi)
date: 2020-04-03T01:59:33+05:30
author: Karhtik Mahendra
avatar: /me.png
authorlink: https://ikarthikmb.github.io
cover: /posts/rpi_ethernet/rpi_thumb01.jpg
categories:
  - posts
tags:
  - raspberry pi
  - ethernet
  - howto
nolastmod: true
draft: false
---

<!-- ![](/posts/rpi_ethernet/rpi_thumb01.jpg) -->

**Contents**


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=true} -->

<!-- code_chunk_output -->

- [Hardware Requirements:](#hardware-requirements)
- [Steps to install the required software tools](#steps-to-install-the-required-software-tools)
  - [Step-1: OS Download](#step-1-os-download)
  - [Step-2: Imager](#step-2-imager)
  - [Step-3: SSH Client Download](#step-3-ssh-client-download)
  - [Step-4: Real VNC Viewer](#step-4-real-vnc-viewer)
  - [Step-5: Image Burning](#step-5-image-burning)
  - [Step-6: ssh](#step-6-ssh)
  - [Step-7: Power](#step-7-power)
  - [Step-8: Network Connections](#step-8-network-connections)
  - [Step-9: SSH Configuration](#step-9-ssh-configuration)
  - [Step-10: Authentication](#step-10-authentication)
  - [Step-11: Pi Terminal](#step-11-pi-terminal)
- [Accessing Pi Desktop Remotely](#accessing-pi-desktop-remotely)

<!-- /code_chunk_output -->

---

In this we shall be working with Raspberry Pi 4 Model-B of 1Gb RAM for the set up. Raspberry-Pi is a single board computer used for educational purposes and DIY projects with an affordable cost, requires a power supply of 5 volts with 3 amps current.  


Operating Systems like Raspbian OS, Windows, Linux, RISC OS, can be installed into it. The Pi 4 model has Ethernet, wireless adapter, USB type-C port, and 40 GPIO(General Purpose Input Output) pins. Unlike the older versions the performance has very much improved with the "Pi 4" model.


## Hardware Requirements:

1. Raspberry Pi 4 Model B (1/2/4 GB RAM)     
2. USB Type-C power supply     
3. Ethernet cable (1 meter)     
4. Personal computer


## Steps to install the required software tools

### Step-1: OS Download
 
From the official raspberrypi.org[^1] download the **Raspbian Buster** operating system

[^1]: https://www.raspberrypi.org/software/

### Step-2: Imager

Also download the **Raspberry Pi Imager**[^2] from the same website, this is for writing the image file onto the SD card.

[^2]: [Raspberry Pi Imager](https://www.raspberrypi.org/software/)

![Raspberry pi OS selection](/posts/rpi_ethernet/pios_site.png)

### Step-3: SSH Client Download

If you are using windows you probably have to download the ssh client, I prefer downloading Bitvise ssh client from PuTTY[^3].

[^3]: [PuTTY](https://putty.org/)

![PuTTY](/posts/rpi_ethernet/putty.png)

### Step-4: Real VNC Viewer

To access the desktop of the pi, you can either connect a micro to HDMI connector from the pi to a monitor or you can access it remotely on your PC/laptop. To connect remotely VNC-server has to be installed onto the pi by default the VNC-server is installed within the operating system, in order to view it remotely one has to download VNC-Viewer[^4] on his/her Desktop.

[^4]: [real vnc-viever website](https://www.realvnc.com/en/connect/download/viewer/)

![vnc viewer website](/posts/rpi_ethernet/vnc_site.png)

### Step-5: Image Burning

Open the Raspberry Pi Imager and select the custom setup then select the OS from the Downloaded folder and carefully set the target as USB drive. Wait for the image to be written on the drive.

![](/posts/rpi_ethernet/imager1.png)| ![](/posts/rpi_ethernet/imager2.png)  | ![](/posts/rpi_ethernet/imager3.png)  
--- | --- | ---
1 | 2  | 3


![](/posts/rpi_ethernet/imager4.png)| ![](/posts/rpi_ethernet/imager5.png)
--- | --- 
4 | 5  

### Step-6: ssh

After done, open the boot folder, create a new document named `ssh` without any extensions, save and then *unmount* the drive.

![save as 'ssh' file](/posts/rpi_ethernet/ssh.png)

### Step-7: Power 

Now connect the Ethernet cable to your PC/lap and power up the pi with the type-C cable.

![](/posts/rpi_ethernet/cable1.png)| ![](/posts/rpi_ethernet/cable2.png) | ![](/posts/rpi_ethernet/cable3.png)
--- | --- | ---

### Step-8: Network Connections

If you are using Windows 10 go to **Control Panel --> Network** and **Internet --> Network Connections**, right-click on Wi-Fi select **properties**, go to **sharing** section and check on “Allow other network users to connect through this computer’s Internet connection”. Make sure that Home network connection is **Ethernet**. Save and close the window.

![](/posts/rpi_ethernet/network1.png) | ![](/posts/rpi_ethernet/network2.png)
--- | ---

### Step-9: SSH Configuration

Open the Bitvise SSH Client, enter `raspberrypi.local` or the IP address(from previous step) as host and leave **22** as default port in the server section.


### Step-10: Authentication

Click Log in and enter username as pi and the default password as **raspberry**. A terminal pops up and you are now into the Raspberry Pi.

![](/posts/rpi_ethernet/pilocal1.png) | ![](/posts/rpi_ethernet/pilocal2.png)
--- | ---

### Step-11: Pi Terminal

If this is your first time logging into pi make sure to update your pi by issuing the command `sudo apt-get update` and then `sudo apt-get upgrade` to upgrade.

![](/posts/rpi_ethernet/terminal1.png)

![](/posts/rpi_ethernet/terminal2.png)

> **Quick tip:** Don’t forget to change your password once you are log in.

## Accessing Pi Desktop Remotely

- Go to terminal and type `vncserver`, notedown the generated ip address. Now open VNC-Viewer on your desktop and enter the **ip address**or paste it, after few seconds a window pops sharing the screen of raspberry pi.

![](/posts/rpi_ethernet/terminal3.png)

- Enter the ip address given by `vncserver` from the raspberry pi to vncviewer application on your pc. 
![VNC viewer screen](/posts/rpi_ethernet/vncviewer1.png)

Enter the username and password on the authentication prompt. 
![Enter the server password](/posts/rpi_ethernet/vncviewer2.png)

- Welcome! to Pi's desktop.
![Raspberry pi desktop](/posts/rpi_ethernet/pidesktop.png)

- This article was originally published in instructables website[^5].

[^5]: [Set Up Raspberry Pi 4 Through Laptop/pc Using Ethernet Cable(No Monitor, No Wi-Fi)](https://www.instructables.com/Set-Up-Raspberry-Pi-4-Through-Laptoppc-Using-Ether/)
