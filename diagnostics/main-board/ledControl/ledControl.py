"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: ledControl.py
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: Checking Internet status LEDs
"""

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pin 29 amd 33 to be an output pin and set initial value to low (off)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)  # Red LED
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)  # Green LED
i = 0
while i < 3:  # Run 3 times
    GPIO.output(29, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(29, GPIO.LOW)  # Turn off
    sleep(1)  # Sleep for 1 second
    GPIO.output(33, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(33, GPIO.LOW)  # Turn off
    sleep(1)  # Sleep for 1 second
    i += 1
print("LED blinking complete")
