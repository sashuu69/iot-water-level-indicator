import pyrebase  # python library for firebase
from datetime import datetime, timedelta
from time import sleep  # Import the sleep function from the time module
config = {  # configuration for connection
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com",
}

firebase = pyrebase.initialize_app(config)  # firebase connection object
db = firebase.database()  # firebase database initialisation

# To create and update sensor-values table
# db.child("sensor-values").update(
#     {"water-tank-percentage": "70",
#      "pump-status": "false",
#      "moisure-percentage": "50",
#      "garden-valve": "false",
#      "tank-valve": "false",
#      "any-valve-open": "false",
#      "farm-valve": "false",
#      "farm-irrigation-time-on": "11:00",
#      "farm-irrigation-time-off": "11:15"}
# )

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

while True:
    # TO get values from table
    timeForIrrigation = db.child(
        "sensor-values").child("farm-irrigation-time-on").get().val()
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    timeFormat = datetime.strptime(timeForIrrigation, "%H:%M")
    print("old time:-")
    print(timeFormat.strftime("%H:%M"))
    timeFormat = timeFormat + datetime.timedelta(minutes=10)
    print("New time:-")
    print(timeFormat.strftime("%H:%M"))
    sleep(1)
