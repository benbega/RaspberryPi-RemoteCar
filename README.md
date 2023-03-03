# RaspberryPi-RemoteCar
Repository hosting code for my RC car project based on the Raspberry Pi 4B+

## **Introduction**

This is a remote controlled car based on two Raspberry Pi 4B+ single board computers. The car chassis is from an old kit for collegiate competitions that I got for free from my university electronics stockroom. The car is powered by 2 7V DC motors, capable of approximately 23,000 RPM without a load.

A more robust document with project details will be posted as a PDF in this repository soon, containing a list of the exact hardware being used and instructions to setup the project yourself.

[A video of the project's current state can be found by clicking here](https://drive.google.com/file/d/16IPjEnowMKMXTBlExd92VV3uJnW5QUr4/view?usp=share_link) 

## **Car Setup**

The car portion of the project contains a chassis, two DC motors, a servo, a Raspberry Pi 4B+, and a custom PCB. The PCB was fully custom designed, and incorporates an L293D motor driver chip, as well as indicator LEDs, signal pins for the servo, and hookups for the system's battery. The car uses a small 7V battery to power all of the microelectronic components, as well as a 5V 3A battery pack to power the Raspberry Pi. Although the dual battery system is extremely heavy and inefficient, it was chosen to suit the Raspberry Pi's high current demands.

## **Wireless Communication**

The wireless controller functionality is implemented by utilizing the Raspberry Pi's remote GPIO functionality through the gpiozero library. The Raspberry Pi powering the controller is setup to be a wireless access point, which the car's Raspberry Pi connects to automatically upon boot. This allows the Remote GPIO setup to work anywhere, not just in specific locations that have a prexisting WiFi network. While lower power Raspberry Pi models, or microcointrollers could likely be used to accomplish the same functionality, these are the boards I currently have, and there is no reason currently to change the design.

## **State of the Project**

The project is currently in a complete state, where all systems are functional as originally designed. The car is able to freely drive and steer, and starts in a driveable state upon boot. The car is heavier than originally designed due to the Raspberry Pi power supply, so the top speed is relatively low.

## **Looking Forward**

I do not currently have plans to update this project, as I am focusing on something else I will write about soon, but in the future my goal is to switch out the motors and servo for significantly more powerful options, and utilize a more efficient LiPo battery pack. A related near term project I plan on completing is a short, detailed write up on how the Raspberry Pi Remote GPIO is setup, as I think it is one of the more interesting aspects of the overall design.

--

This project is licensed under the terms of the MIT license