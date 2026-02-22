# vl53l5cx_for_PICO_Pi_in_Micropython_Code
Quick drop-in rev of vl53l5cx Lidar Code in Micrpython for PICO Pi Board.

This is a group of files for copying onto PICO Pi Directiory with Thonny.

I spent a large chunk of timde trying to figure out how to use the vl53l5cx Lidar on PICO or arduino.
Arduino Uno/Nano can't do this because a chunk of RAM is needed to process the readings.

But, code for the PICO kept refeing back to Pimoroni code / Breakout_vl53l5cx :
  https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/breakout_vl53l5cx/vl53l5cx_demo.py
Which is not correct , because this code is built to run on Linux on raspberry Pi, and the PICO can not support this code (no Linux and too many files for the flash).

-

The Code is actually from : 
https://github.com/mp-extras/vl53l5cx

The support code (which needs to be dropped into PICO as dir /vl53l5cx) :
https://github.com/mp-extras/vl53l5cx/tree/main/vl53l5cx

And, best working code for the Lidar :
https://github.com/mp-extras/vl53l5cx/blob/main/examples/basic.py

-

This code rev is simple.  Copy the dir /vl53l5cx onto the PICO - with Thonny.
And, add basic.py onto the main dir / to execute.
This file can be modified - to return readings to other calling code files.

-

Hope this helps people to use the Lidar vl53l5cx easily on PICO now !

---
