"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: relayTest.py
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: Checking pump relays
"""

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep  # Import the sleep function from the time module
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
# Set pin 7,11 to be an output pin and set initial value to low (off)
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)  # Relay 1
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)  # Relay 2
i = 0
while i < 3:  # Run forever
    GPIO.output(7, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(7, GPIO.LOW)  # Turn off
    sleep(1)  # Sleep for 1 second
    GPIO.output(11, GPIO.HIGH)  # Turn on
    sleep(1)  # Sleep for 1 second
    GPIO.output(11, GPIO.LOW)  # Turn off
    sleep(1)  # Sleep for 1 second
    i += 1
print("Relay switching complete")
