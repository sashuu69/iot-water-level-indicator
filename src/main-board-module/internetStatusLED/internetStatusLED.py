"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : internetStatusLED.py
 * Author : Sashwat K
 * Created on : 18 Oct 2019
 * Last updated : 17 Nov 2019
 * Single Board Computer : Raspberry Pi Zero W
 * Purpose : Checking connection to firebase.google.com and represent it with LEDs.
"""

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import socket  # Library to include socket functions
from time import sleep  # Import the sleep function from the time module

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering

# URL to which the connection to be tested
REMOTE_SERVER = "firebase.google.com"

# Set pin 29 amd 33 to be an output pin and set initial value to low (off)
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW)  # Red LED
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)  # Green LED

"""Definition to check connection status to firebase. The function is boolean."""


def isConnected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


def ledStatus(connectionStatus):
    try:
        if connectionStatus == True:
            GPIO.output(33, GPIO.HIGH)  # Turn on Green
            GPIO.output(29, GPIO.LOW)  # Turn off Red
            print("Connected")

        else:
            GPIO.output(33, GPIO.LOW)  # Turn off Green
            GPIO.output(29, GPIO.HIGH)  # Turn on Red
            print("Not connected")
    except:
        pass


while True:
    ledStatus(isConnected(REMOTE_SERVER))
    sleep(1)
