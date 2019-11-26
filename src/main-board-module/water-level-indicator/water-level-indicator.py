"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : water-level-indicator.py
 * Author : Sashwat K & Vijitha V Nair
 * Created on : 10 Oct 2019
 * Last updated : 17 Nov 2019
 * Single Board Computer : Raspberry Pi Zero W
 * Purpose : The main controller
 * Pins used : Relay - 7
"""

import RPi_I2C_driver  # LCD driver
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import os  # for running bash commands
import subprocess  # For returning bash commands
from time import sleep  # for getting realtime
from datetime import datetime, timedelta  # for date and time
import pyrebase  # python library for firebase
from dotenv import load_dotenv  # for accessing environment (.env) file

systemLCD = RPi_I2C_driver.lcd()  # initialse LCD driver
GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)  # Relay pin initialisation
tankModuleAdress = 0x05  # Arduino tank module address
valveModuleAddress = 0x04  # Arduino valve cmodule address
load_dotenv()  # load environment (.env) file
# configuration for connection
configurationForFirebase = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "storageBucket": os.getenv("storageBucket"),
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
        systemLCD.lcd_display_string_pos("Program closed", 1, 2)
        systemLCD.lcd_display_string_pos("Error code 1", 2, 2)
    except:
        pass


# Function to send values to firebase
def sendValuesToFirebase(valveWorking, garden, moisPer, relayTrig, tank, tpCntPer, farm, manuFlag):
    try:
        databaseObject.child("sensor-values").update(
            {"water-tank-percentage": tpCntPer,
             "pump-status": relayTrig,
             "moisure-percentage": moisPer,
             "garden-valve": garden,
             "tank-valve": tank,
             "farm-valve": farm,
             "any-valve-open": valveWorking,
             "manual-flag": manuFlag, }
        )
    except:
        pass


# Defition to enter log to firebase
def dataLog(logDate, logTime, actionResult):
    try:
        databaseObject.child("log").child(logDate).child(logTime).set(
            {"action": actionResult}
        )
    except:
        pass


def dailyLogCount(action, valueE):
    try:
        databaseObject.child("daily-usage").update(
            {action: valueE}
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
    tempFlagForLog = False
    farmValveFlag = False
    while True:  # runs forever
        try:
            i = i + 1  # iteration purpose
            # Initalisation of values from firebase
            print("Retriving data from firebase....")
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
            manualTrigger = databaseObject.child(
                "sensor-values").child("manual-flag").get().val()
            dailyFarm = int(databaseObject.child(
                "daily-usage").child("farm").get().val())
            dailyGarden = int(databaseObject.child(
                "daily-usage").child("garden").get().val())
            dailyPump = int(databaseObject.child(
                "daily-usage").child("pump").get().val())
            dailyTank = int(databaseObject.child(
                "daily-usage").child("tank").get().val())
            print("Data retrived..")
            now = datetime.now()  # get current time
            current_time = str(now.strftime("%H:%M"))  # convert to hour:minute
            # convert to year/month/day
            current_date = str(now.strftime("%Y/%m/%d"))
            # convert time to hour:minute:seconds for log
            timeForLog = str(now.strftime("%H:%M:%S"))
            # get touch pad count from tank module
            tpCnt = i2cReceiveCommand(tankModuleAdress, 111)
            tpCntPer = int(tpCnt * 100 / 4)  # count to percentage
            # get distance from tank module
            ultrasnc = i2cReceiveCommand(tankModuleAdress, 222)
            # get moisure percentage from valve module
            moisPer = getMoisurePer(valveModuleAddress)

            # For manual control from app
            # check for manual operation and if any valve not working
            if manualTrigger == True and valveWorking == False:
                valveControlSig(1)  # Open valve tank (valve 1)
                valveWorking = True  # Valve engaged flag
                relayControl(1)  # Turn ON pump
                relayTrig = True  # Pump status flag
                tank = True  # tank valve flag
                # Logging to firebase
                if tempFlagForLog == False:  # For displaying once
                    dailyPump += 1
                    dailyLogCount("pump", dailyPump)
                    dailyTank += 1
                    dailyLogCount("tank", dailyTank)
                    dataLog(current_date, timeForLog,
                            "Manual Tank Pump Activated")
                    tempFlagForLog = True

            # For water tank
            if tpCntPer == 0:  # triggered at 0% water level
                if valveWorking == False:  # check if any valve open
                    valveControlSig(1)  # Open valve tank (valve 1)
                    valveWorking = True  # Valve engaged flag
                    relayControl(1)  # Turn ON pump
                    relayTrig = True  # Pump status flag
                    tank = True  # tank valve flag
                    # Logging into firebase
                    if tempFlagForLog == False:  # For displaying once
                        dailyPump += 1
                        dailyLogCount("pump", dailyPump)
                        dailyTank += 1
                        dailyLogCount("tank", dailyTank)
                        dataLog(current_date, timeForLog,
                                "Tank Pump Activated")
                        tempFlagForLog = True
            elif tpCntPer == 100 and ultrasnc < 20:  # Triggered at 100% water level and distance less than 20
                valveControlSig(0)  # Close valve tank
                valveWorking = False  # Valve disengaged flag
                relayControl(0)  # Turn OFF pump
                relayTrig = False  # Pump status flag
                tank = False  # tank valve flag
                manualTrigger = False  # Set manual flag to OFF
                # Logging into firebase
                if tempFlagForLog == True:
                    dataLog(current_date, timeForLog,
                            "Tank Pump Deactivated")
                    tempFlagForLog = False
            # For sprinkler system
            if moisPer < 10:  # if mosiure less than 30%
                if valveWorking == False:  # check if any valve open
                    valveControlSig(2)  # Open valve garden (valve 2)
                    valveWorking = True  # Valve working flag
                    relayControl(1)  # pump ON
                    relayTrig = True  # Valve flag
                    garden = True  # garden valve flag
                    if tempFlagForLog == False:
                        dailyPump += 1
                        dailyLogCount("pump", dailyPump)
                        dailyGarden += 1
                        dailyLogCount("garden", dailyGarden)
                        dataLog(current_date, timeForLog,
                                "Garden Sprinkler Activated")
                        tempFlagForLog = True
            elif moisPer > 50:  # if moisure more than 60
                valveControlSig(0)  # Close valve garden
                valveWorking = False
                relayControl(0)
                relayTrig = False
                garden = False  # garden valve flag
                if tempFlagForLog == True:
                    dataLog(current_date, timeForLog,
                            "Garden Srinkler Deactivated")
                    tempFlagForLog = False

            # For farm
            if current_time == timeForIrrigationON:  # check current time with farm trigger time
                if farmValveFlag == False:  # flag to execute the following code once until farm valve is closed
                    if valveWorking == False:  # check if any valve open
                        valveControlSig(3)  # Open valve farm (valve 3)
                        relayControl(1)  # Pump ON
                        valveWorking = True
                        relayTrig = True
                        farm = True  # farm valve flag
                        farmValveFlag = True  # For one execution only
                        if tempFlagForLog == False:
                            dailyPump += 1
                            dailyLogCount("pump", dailyPump)
                            dailyFarm += 1
                            dailyLogCount("farm", dailyFarm)
                            dataLog(current_date, timeForLog,
                                    "Farm Sprinkler Activated")
                            tempFlagForLog = True
                    else:
                        # Posepone time by 10 mins
                        postponeStart = datetime.strptime(
                            timeForIrrigationON, "%H:%M") + timedelta(minutes=10)
                        postponeEnd = datetime.strptime(
                            timeForIrrigationOFF, "%H:%M") + timedelta(minutes=10)
                        # update in firebase
                        databaseObject.child("sensor-values").update(
                            {"farm-irrigation-time-on": postponeStart.strftime("%H:%M"),
                             "farm-irrigation-time-off": postponeEnd.strftime("%H:%M")}
                        )
            if current_time == timeForIrrigationOFF:  # check if off time
                valveControlSig(0)  # Close valve farm (valve-3)
                relayControl(0)  # pump OFF
                valveWorking = False
                relayTrig = False
                farm = False  # farm valve flag
                farmValveFlag = True
                # Update original time
                databaseObject.child("sensor-values").update(
                    {"farm-irrigation-time-on": "11:00",
                     "farm-irrigation-time-off": "11:15"}
                )
                # Logging to firebase
                if tempFlagForLog == True:
                    dataLog(current_date, timeForLog,
                            "Farm Sprinkler Deactivated")
                    tempFlagForLog = False

            mainLCDConsole(tpCntPer, relayTrig)  # Values to display on LCD
            # Store relavent sensor data in firebase
            sendValuesToFirebase(valveWorking, garden,
                                 moisPer, relayTrig, tank, tpCntPer, farm, manualTrigger)
            # display necessary data
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
            print("Manual control: " + str(manualTrigger))
            print("---------------------------------------")
        except (KeyboardInterrupt, SystemExit):  # when control + c is encountered
            print("\nClosing program..")
            valveControlSig(0)  # Set valve as OFF
            relayControl(0)  # Turn off pump
            exitConsole()  # Display stuff on LCD
            sendValuesToFirebase(False, False,
                                 0, False, False, 0, False, False)  # reset all values in firebase for consistency
            exit()  # Exit program


# 1st execution
if __name__ == '__main__':
    main()
