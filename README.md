DogeFetch
==============

A physical bot that tracks realtime DOGE values and address balances.

Uses a Raspberry Pi and an IC2-based LED display.

Programmed in Python. (see main.py)

Currently a WIP.

Do It Yourself
==============

You will need:

 - Soldering Iron and Solder Wire
 - Raspberry Pi Model B
 - Adafruit 16x2 Character LCD + Keypad for Raspberry Pi (https://www.adafruit.com/products/1110)
 - Raspbian OS


1. Solder the LCD PCB using the tutorial here: http://learn.adafruit.com/adafruit-16x2-character-lcd-plus-keypad-for-raspberry-pi
2. Set up IC2 using this tutorial: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
3. Run "sudo apt-get install python-smbus & sudo apt-get install i2c-tools" on bash
4. To make sure your LCD is connected, run "sudo i2cdetect -y 1" and look for the "0x20" query
5. If it is not connected, unplug it from your Pi and make sure you have soldered each wire correctly.
6. Run "sudo apt-get install python-dev & sudo apt-get install python-rpi.gpio"
7. Download "/code/" from the repository
8. Run "sudo python DogeFetch.py"
