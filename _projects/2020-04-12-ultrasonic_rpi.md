---
title: Intruder Detection Using Pi Camera
date: 2020-04-12
author: Karhtik Mahendra
avatar: me.png
authorlink: https://ikarthikmb.github.io
cover: /projects/intruder_rpi/circuit_intruder_rpi.png
excerpt: >
  Build a DIY intruder detection system using Raspberry Pi, a Pi Camera, and a PIR motion sensor. Capture photos automatically when motion is detected, enabling simple and effective home security monitoring.

categories:
  - projects
tags:
  - raspberry pi
  - sensors
  - circuits
nolastmod: true
draft: false
---

![circuit_intruder_rpi](/static/projects/intruder_rpi/circuit_intruder_rpi.png)

**Contents**


<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=true} -->

<!-- code_chunk_output -->

- [Hardware](#hardware)
- [Circuit Connection](#circuit-connection)
- [The Code](#the-code)
- [Youtube Video Tutorial:](#youtube-video-tutorial)

<!-- /code_chunk_output -->

---

This project is about capturing the pictures of strangers through the Pi Camera attached to Raspberry Pi. This is a DIY project which can detect people using the motion sensor(PIR sensor) by capturing a photo whenever the motion is detected.

## Hardware

1. Raspberry Pi 2/3/4
2. Pi Camera
3. PIR Sensor
4. Jumpers

## Circuit Connection

![Connecting PIR sensor to Raspberry Pi 3](/static/projects/intruder_rpi/circuit_intruder_rpi.png "Connecting PIR sensor to Raspberry Pi")

[![Connecting Pi Camera to Raspberry Pi, Source: raspberrypi.org](/static/projects//intruder_rpi/connect-picamera-rpi.gif)](https://projects-static.raspberrypi.org/projects/getting-started-with-picamera/eb7defb950e2f3eeb8aa5934d26cfd600860c8a0/en/images/connect-camera.gif)

 Connect the PIR sensor to raspberry pi as shown in the above circuit diagram. Additionally connect the Pi Cam to Raspberry Pi camera port. To check whether your camera is working or not **run** the following code. 

```
raspistill -o Desktop/image.jpg
```

Apparantly, you should  see the `image` saved on your Desktop, if not make sure you connected the camera properly and **restart** the device.

## The Code

Save the below code as `pir-camera-test.py` and run. 

```

   #Code for Capturing Strangers:

   from gpiozero import MotionSensor
   from picamera import PiCamera
   import RPi.GPIO as GPIO
   import time

   GPIO.setmode(GPIO.BCM)
   GPIO.setwarnings(False)

   pir=MotionSensor(23)
   camera=PiCamera()
   camera.rotation = 180
   camera.start_preview()

   while True:
    GPIO.setup(24, GPIO.OUT)
    if pir.wait_for_motion():
        GPIO.output(24, GPIO.HIGH)
        #time.sleep(0.1)
        print("Motion Detected")
        camera.capture('/home/pi/Marvel/PiCam/PiImage/Strangers/image-'+ time.ctime()+'.png')
         print("image-"+time.ctime())
         GPIO.output(24, GPIO.LOW)

    else:
        print("Motion not Detected")
    time.sleep(3)
   camera.stop_preview()
   camera.close()
```


## Youtube Video Tutorial:

[![Youtube Tutorial Video](/static/projects//intruder_rpi/intruder_ytthumb.png)](https://youtu.be/Nw-yHMn69R0?t=47)[^1]

You can rewrite the code and change the parameters for your requirements. If you have suggestions or any trouble with the project, feel free to comment below. Happy Circuiting!

[^1]: https://youtu.be/Nw-yHMn69R0?t=47
