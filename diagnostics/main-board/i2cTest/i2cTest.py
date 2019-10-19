"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: relayTest.py
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: Checking I2C Communication
"""
import smbus
import time

bus = smbus.SMBus(1)
address = 0x05
number = read_byte(address)
print(number)
