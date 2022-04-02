# RaspberryPi-RemoteCar
Repository hosting code for my RC car project based on the Raspberry Pi 4B+

**Introduction**

This is a remote controlled car based on two Raspberry Pi 4B+ single board computers. The car chassis is from an old kit for collegiate competitions that I got for free from my university electronics stockroom. The car is powered by 2 DC motors that run off of any voltage between 3.0 and 7.4 Volts, capable of approximately 23,000 RPM without a load.

A more robust document with project details will be posted as a PDF in this repository soon, containing a list of the exact hardware being used and instructions to setup the project yourself.

**Wireless Communication**

The wireless controller functionality is implemented by utilizing the Raspberry Pi's remote GPIO functionality through the gpiozero library. While lower power Raspberry Pi models could likely be used to accomplish the same functionality, these are the boards I currently have, and there is no reason currently to change the design.

**State of the Project**

The project is currently in pretty early stages of development, with the repository only hosting files used to test the motors and remote GPIO functionality.

**Looking Forward**

Over the course of the next few weeks, I will be adding support for user input to control the steering servo and motor power. After all of the basic driving functionality is implemented, I will work on creating an automated system for automatically starting scripts on the Raspberry Pis and connecting the remote GPIO functionality.