---
layout: post
title: Measuring Soil Moisture using Raspberry Pi
date: 2020-03-29
author: Karhtik Mahendra
avatar: /me.png
authorlink: https://ikarthikmb.github.io
cover: /projects/soil_moisture_rpi_fig/soil-moisture-circuit.jpg
excerpt: >
  Learn how to measure soil moisture using a Raspberry Pi and a simple sensor circuit. This project walks through hardware setup, wiring using MCP3008 ADC, and Python code to monitor real-time moisture levels—ideal for smart gardening or home automation.

categories:
  - projects
tags:
  - raspberry pi
  - sensors
  - circuits
nolastmod: true
draft: false
---

![soil-moisture-circuit](/static/projects/soil_moisture_rpi_fig/soil-moisture-circuit.jpg)

Do you know how often to water plants? Or outpoured plants and lost them. To solve this I thought it would be more circumstantial if we can get the value of water content inside the soil in order to make a decision for watering the plants appropriately.

In this project lets try to build a circuit which can measure the water content value of the soil eventually control the flow using Raspberry Pi.

## Hardware:
- Raspberry Pi 2/3/4
- Soil moisture sensor
- MCP3008
- Jumpers

## Circuit Connection:
 
![Circuit connections](/static/projects/soil_moisture_rpi_fig/soil-moisture-circuit.jpg)


1. MCP3008 GND to GND
2. MCP3008 CS to RPI 8
3. MCP3008 DIN to RPI 10
4. MCP3008 DOUT to RPI 9
5. MCP3008  CLK to RPI 11
6. MCP3008 AGND to GND
7. MCP3008 VREF to +3V
8. MCP3008 VCC to +3V
9. SoilMoisture A0 to MCP3008 CH0
10. SoilMoisture VCC to +3V
11. SoilMoisture GND to GND 

Make all the connections and power up the Raspberry Pi. If you want to learn how to connect a Raspberry Pi check out my previous post on how to [Set Up Raspberry Pi 4 Through Laptop/pc Using Ethernet Cable(No Monitor, No Wi-Fi)](https://ikarthikmb.github.io/posts/rpi4_setup_w_ethernet/)[^1].

[^1]: https://ikarthikmb.github.io/posts/rpi4_setup_w_ethernet/

### Essential Packages
Before you run the code you have to install few libraries, move on with the following steps.

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
[sudo](sudo) python setup.py install
```

## The Code
Once the library has been installed it's time to execute the code. You can use the below code or download it from [here](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/RaspberryPi/moist-soil.py)[^2].

[^2]: https://github.com/Ikarthikmb/Hardware-Codes/blob/master/RaspberryPi/moist-soil.py

```
import RPi.GPIO as GPIO
from time import sleep

import Adafruit_MCP3008

am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

while True:
  moisture_value = am.read_adc(0)
  per = moisture_value * 100 / 1023
  print("Recorded moisture value is %s percentage" % per)
  if moisture_value >= 930:
    print(" No water, Can you plaease water me")
  elif moisture_value < 930 and moisture_value >= 350:
    print(" I'm sufficient ")
  elif moisture_value < 350 :
    print(" Stop drowning me!")
  sleep(1.5)

```

## Youtube Video Tutorial:

youtube ahQhEWf1PRI

[![](/static/projects/soil_moisture_rpi_fig/soilmoisture_youtubethumb.png)](https://youtu.be/ahQhEWf1PRI "Click to play")


You can rewrite the code and change the parameters for your requirements. If you have suggestions or any trouble with the project, feel free to comment below. Happy Circuiting!
