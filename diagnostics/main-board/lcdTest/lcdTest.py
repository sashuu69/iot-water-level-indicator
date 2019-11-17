"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : ledTest.py
 * Author : Sashwat K
 * Created on : 18 Oct 2019
 * Last updated : 17 Nov 2019
 * Single Board Computer : Raspberry Pi Zero W
 * Purpose : Checking I2C LCD
"""

import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

mylcd.lcd_display_string("Sashwat's Lab", 1)
