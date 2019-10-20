"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: water-level-indicator.py
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 20 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: The main controller
"""

import RPi_I2C_driver  # LCD driver
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import os  # for running bash commands
import subprocess  # For returning bash commands
from time import sleep  # for getting realtime
from datetime import datetime  # for date and time

systemLCD = RPi_I2C_driver.lcd()  # initialse LCD driver
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)  # Relay pin initialisation
tankModuleAdress = 0x05  # Arduino tank module address
valveModuleAddress = 0x04  # Arduino valve cmodule address


# Function to send values through I2C from Pi to arduino using bash
def i2cSendCommand(address, value):
    try:
        bashCommand = 'i2cset -y 1 ' + str(address) + ' ' + str(value)
        os.system(bashCommand)
        return True
    except:
        pass
    return False


# Function to receive values through I2C from Pi to arduino using bash
def i2cReceiveCommand(address, value):
    try:
        sendBashCommand = 'i2cset -y 1 ' + str(address) + ' ' + str(value)
        os.system(sendBashCommand)
        receiveBashCommand = 'i2cget -y 1 ' + str(address)
        bashValue = subprocess.Popen(
            receiveBashCommand, shell=True, stdout=subprocess.PIPE).stdout
        fValue = bashValue.read().strip().decode()
        decimalValue = int(fValue, 16)
        return decimalValue
    except:
        pass


# Function to control relay
def relayControl(statuss):
    try:
        GPIO.output(7, GPIO.HIGH) if statuss == 1 else GPIO.output(7, GPIO.LOW)
    except:
        pass


# Fucntion for LCD boot scren
def ledBootScreen():
    systemLCD.lcd_clear()
    systemLCD.lcd_display_string_pos("Water", 1, 5)
    sleep(0.8)
    systemLCD.lcd_clear()
    systemLCD.lcd_display_string_pos("Level", 2, 5)
    sleep(0.8)
    systemLCD.lcd_clear()
    systemLCD.lcd_display_string_pos("Indicator", 1, 4)
    sleep(0.8)
    systemLCD.lcd_clear()
    systemLCD.lcd_display_string_pos("By,", 1, 5)
    sleep(0.5)
    systemLCD.lcd_clear()
    systemLCD.lcd_display_string_pos("Sashwat K &", 1, 0)
    systemLCD.lcd_display_string_pos("Vijitha V Nair", 2, 0)
    sleep(0.5)
    systemLCD.lcd_clear()


def getUltrasonicValue():
    try:
        ultdis = i2cReceiveCommand(tankModuleAdress, 222)
        return ultdis
    except:
        pass


def valveControlSig(valuev):
    try:
        i2cReceiveCommand(valveModuleAddress, valuev)
    except:
        pass


# Function to show the main console
def mainLCDConsole(waterLevel, relayS, gardenS, farmS, tankS):
    for i in range(0, 15):
        addDateTime = "Time: " + datetime.now().strftime("%H:%M:%S")  # get time
        waterPercentage = "Water Level: " + \
            str(waterLevel) + " %"  # get water level
        # Relay status
        if relayS == 0:
            relayStat = "Pump: OFF"
        else:
            relayStat = "Pump: ON"
        # Garden sprinkler valve status
        if gardenS == 0:
            gardenStat = "Gardn valve: OFF"
        else:
            gardenStat = "Gardn valve: ON"
        # Farm sprinkler valve status
        if farmS == 0:
            farmStat = "Farm valve: OFF"
        else:
            farmStat = "Farm valve: ON"
        # tank valve status
        if tankS == 0:
            tankStat = "Tank valve: OFF"
        else:
            tankStat = "Tank valve: ON"

        if i < 3:
            systemLCD.lcd_clear()
            systemLCD.lcd_display_string(addDateTime, 1)
            systemLCD.lcd_display_string(waterPercentage, 2)
        if i >= 3 and i < 6:
            systemLCD.lcd_clear()
            systemLCD.lcd_display_string(addDateTime, 1)
            systemLCD.lcd_display_string(relayStat, 2)
        if i >= 6 and i < 9:
            systemLCD.lcd_clear()
            systemLCD.lcd_display_string(addDateTime, 1)
            systemLCD.lcd_display_string(gardenStat, 2)
        if i >= 9 and i < 12:
            systemLCD.lcd_clear()
            systemLCD.lcd_display_string(addDateTime, 1)
            systemLCD.lcd_display_string(farmStat, 2)
        if i >= 12 and i < 15:
            systemLCD.lcd_clear()
            systemLCD.lcd_display_string(addDateTime, 1)
            systemLCD.lcd_display_string(tankStat, 2)
        sleep(1)


# Main function
def main():
    ledBootScreen()
    while True:
        try:
            relayTrig = 0  # for displaying relay stat in LCD
            tank = 0  # for displaying tank valve stat in LCD
            farm = 0  # for displaying farm valve stat in LCD
            garden = 0  # for displaying garden valve stat in LCD
            valveWorking = 0  # Check if any valve is working or not
            tpCnt = 1 #i2cReceiveCommand(tankModuleAdress, 111)
            tpCntPer = int(tpCnt * 100 / 4)
            ultrasnc = i2cReceiveCommand(tankModuleAdress, 222)
            print(tpCntPer)
            mainLCDConsole(tpCntPer,
                           0, 0, 0, 0)
            if tpCntPer == 0:
                valveControlSig(1)
                valveWorking = 1
                relayControl(1)
                relayTrig = 1
                tank = 1
                # display all details in LCD

            elif tpCntPer == 100 and ultrasnc < 10:
                valveControlSig(0)
                valveWorking = 0
                relayControl(0)
                relayTrig = 0
                tank = 0
                # display all details in LCD
            # farmTime = datetime.now().strftime("%H:%M:%S")
            # if valveWorking == 1:
            #     if farmTime == '17:40:00':
        except:
            pass


# 1st execution
if __name__ == '__main__':
    main()
