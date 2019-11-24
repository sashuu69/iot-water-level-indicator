"""
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : firebase-connection.py
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Nov 2019
 * Single Board Computer : Raspberry Pi Zero W
 * Purpose : Checking Firebase Connection
"""

import pyrebase  # python library for firebase
import os  # OS python library for running level commands
from datetime import datetime, timedelta
from time import sleep  # Import the sleep function from the time module
from dotenv import load_dotenv  # for accessing environment (.env) file

load_dotenv()  # load environment (.env) file

config = {  # configuration for connection
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "storageBucket": os.getenv("storageBucket"),
}

firebase = pyrebase.initialize_app(config)  # firebase connection object
db = firebase.database()  # firebase database initialisation

# To create and update sensor-values table
db.child("daily-usage").update(
    {"farm": "0",
     "garden": "0",
     "pump": "0",
     "tank": "0", }
)

# To create and update log table
# db.child("log").child("2019/10/13").child("10:15").update(
#     {"action": "Pump on"}
# )
# db.child("log").child("2019/10/13").child("10:30").update(
#     {"action": "Pump off"}
# )

# To create and update users table
# db.child("users").update(
#     {"username": "vijitha",
#      "password": "password"}
# )

# while True:
#     # TO get values from table
#     timeForIrrigation = db.child(
#         "sensor-values").child("farm-irrigation-time-on").get().val()
#     now = datetime.now()
#     current_time = now.strftime("%H:%M")
#     timeFormat = datetime.strptime(timeForIrrigation, "%H:%M")
#     timeFormat1 = timeFormat + timedelta(minutes=10)
#     print("old time:-")
#     print(timeFormat.strftime("%H:%M"))
#     print("New time:-")
#     print(timeFormat1.strftime("%H:%M"))
#     sleep(1)
