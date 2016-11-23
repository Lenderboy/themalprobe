# themalprobe
Probe for Raspberry Pi slightly modified for vaccine fridge

This is a very important step that is overlooked for Rasp Pi 2 and 3:
Now you need to enter the following at the command prompt:

sudo nano /boot/config.txt
to open the /boot/config.txt file for editing. Then scroll down to the bottom of the file, and add the line:

dtoverlay=w1-gpio
Ctrl-X to save the amended file.
