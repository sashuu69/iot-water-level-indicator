"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: water-level-indicator.py
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 20 Oct 2019
 * Microcontroller: Raspberry Pi Zero W
 * Purpose: The main controller
 * Pins used: Relay - 7
"""

import RPi_I2C_driver  # LCD driver
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import os  # for running bash commands
import subprocess  # For returning bash commands
from time import sleep  # for getting realtime
from datetime import datetime  # for date and time
import pyrebase  # python library for firebase

systemLCD = RPi_I2C_driver.lcd()  # initialse LCD driver
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)  # Relay pin initialisation
tankModuleAdress = 0x05  # Arduino tank module address
valveModuleAddress = 0x04  # Arduino valve cmodule address
# configuration for connection
configurationForFirebase = {
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com",
}
firebaseObject = pyrebase.initialize_app(
    configurationForFirebase)  # firebase connection object
databaseObject = firebaseObject.database()  # firebase database initialisation


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


# Function for LCD boot screen
def ledBootScreen():
    try:
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
        sleep(1)
        systemLCD.lcd_clear()
        systemLCD.lcd_display_string_pos("Loading...", 1, 3)
    except:
        pass


# Function to get ultrasonic sensor value
def getUltrasonicValue():
    try:
        ultdis = i2cReceiveCommand(tankModuleAdress, 222)
        return ultdis
    except:
        pass


# Function to send valve number
def valveControlSig(valuev):
    try:
        i2cSendCommand(valveModuleAddress, valuev)
    except:
        pass


# Function to get moisure sensor percentage
def getMoisurePer(address):
    try:
        receiveBashCommand = 'i2cget -y 1 ' + str(address)
        bashValue = subprocess.Popen(
            receiveBashCommand, shell=True, stdout=subprocess.PIPE).stdout
        fValue = bashValue.read().strip().decode()
        decimalValue = int(fValue, 16)
        return decimalValue
    except:
        pass


# Function to show the main console in LCD
def mainLCDConsole(waterLevel, relayS):
    try:
        waterPercentage = "Water Level: " + \
            str(waterLevel) + " %"  # get water level
        # Relay status
        if relayS == 0:
            relayStat = "Pump: OFF"
        else:
            relayStat = "Pump: ON"
        systemLCD.lcd_clear()
        systemLCD.lcd_display_string(waterPercentage, 1)
        systemLCD.lcd_display_string(relayStat, 2)
    except:
        pass


# Function to handle LCD exit screen
def exitConsole():
    try:
        systemLCD.lcd_clear()
        systemLCD.lcd_display_string_pos("Program", 1, 4)
        systemLCD.lcd_display_string_pos("Closed", 2, 4)
    except:
        pass


# Function to send values to firebase
def sendValuesToFirebase(valveWorking, garden, moisPer, relayTrig, tank, tpCntPer, farm):
    try:
        databaseObject.child("sensor-values").update(
            {"water-tank-percentage": tpCntPer,
             "pump-status": relayTrig,
             "moisure-percentage": moisPer,
             "garden-valve": garden,
             "tank-valve": tank,
             "farm-valve": farm,
             "any-valve-open": valveWorking}
        )
    except:
        pass


# Main function
def main():
    print("###############################################")
    print("#-----Water Level Indicator main code---------#")
    print("###############################################")
    print("Project by Sashwat K and Vijitha V Nair")
    print("Initialising....")
    print("-----------------------------------------------")
    ledBootScreen()  # bootscreen for LCD
    i = 0
    while True:
        try:
            i = i + 1  # iteration purpose
            # Initalisation of values from firebase
            relayTrig = bool(databaseObject.child(
                "sensor-values").child("pump-status").get().val())
            tank = bool(databaseObject.child(
                "sensor-values").child("tank-valve").get().val())
            farm = bool(databaseObject.child(
                "sensor-values").child("farm-valve").get().val())
            garden = bool(databaseObject.child(
                "sensor-values").child("garden-valve").get().val())
            valveWorking = bool(databaseObject.child(
                "sensor-values").child("any-valve-open").get().val())
            timeForIrrigationON = databaseObject.child(
                "sensor-values").child("farm-irrigation-time-on").get().val()
            timeForIrrigationOFF = databaseObject.child(
                "sensor-values").child("farm-irrigation-time-off").get().val()
            now = datetime.now()  # get current time
            current_time = str(now.strftime("%H:%M"))  # convert to hour:minute
            # get touch pad count from tank module
            tpCnt = i2cReceiveCommand(tankModuleAdress, 111)
            tpCntPer = int(tpCnt * 100 / 4)  # count to percentage
            # get distance from tank module
            ultrasnc = i2cReceiveCommand(tankModuleAdress, 222)
            # get moisure percentage from valve module
            moisPer = getMoisurePer(valveModuleAddress)

            # For water tank
            if tpCntPer == 0:
                if valveWorking == False:
                    valveControlSig(1)  # Open valve tank
                    valveWorking = True  # Valve engaged flag
                    relayControl(1)  # Turn ON pump
                    relayTrig = True  # Pump status flag
                    tank = True  # tank valve flag
            elif tpCntPer == 100 and ultrasnc < 10:
                valveControlSig(0)  # Close valve tank
                valveWorking = False  # Valve disengaged flag
                relayControl(0)  # Turn OFF pump
                relayTrig = False  # Pump status flag
                tank = False  # tank valve flag

            # For sprinkler system
            if moisPer < 30:
                # If all valves are closed. Then execute
                if valveWorking == False:
                    valveControlSig(2)  # Open valve garden
                    valveWorking = True
                    relayControl(1)
                    relayTrig = True
                    garden = True
            elif moisPer > 85:
                valveControlSig(0)  # Close valve garden
                valveWorking = False
                relayControl(0)
                relayTrig = False
                garden = False

            # For farm
            if current_time == timeForIrrigationON:
                valveControlSig(3)  # Open valve farm
                relayControl(1)
                valveWorking = True
                relayTrig = True
                farm = True
            elif current_time == timeForIrrigationOFF:
                valveControlSig(0)  # Close valve farm
                relayControl(0)
                valveWorking = False
                relayTrig = False
                farm = False

            mainLCDConsole(tpCntPer, relayTrig)
            sendValuesToFirebase(valveWorking, garden,
                                 moisPer, relayTrig, tank, tpCntPer, farm)

            print("Iteration number: " + str(i))
            print("Time: " + str(current_time))
            print("Water tank touch pad percentage: " + str(tpCntPer))
            print("Water ultrasonic sensor: " + str(ultrasnc))
            print("Pump status: " + str(relayTrig))
            print("Moisure percentage: " + str(moisPer))
            print("Garden valve: " + str(garden))
            print("Farm valve: " + str(farm))
            print("tank valve: " + str(tank))
            print("Any valve open? " + str(valveWorking))
            print("Farm ON Time: " + str(timeForIrrigationON))
            print("Farm OFF Time: " + str(timeForIrrigationOFF))
            print("---------------------------------------")
            sleep(1)
        except (KeyboardInterrupt, SystemExit):
            print("\nClosing program..")
            valveControlSig(0)  # Set valve as OFF
            relayControl(0)  # Turn off pump
            exitConsole()
            sendValuesToFirebase(False, False,
                                 0, False, False, 0, False)
            exit()


# 1st execution
if __name__ == '__main__':
    main()
