import pyrebase  # python library for firebase
from datetime import datetime
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
#      "farm-irrigation-time": "11:00:00"}
# )

# To create and update log table
# db.child("log").child("2019/10/13").child("14:51:50").update(
#     {"action": "Pump on"}
# )

# To create and update users table
# db.child("users").update(
#     {"username": "vijitha",
#      "password": "password"}
# )

# TO get values from table
# timeForIrrigation = db.child(
#     "sensor-values").child("farm-irrigation-time").get().val()

while True:
    timeForIrrigation = db.child(
        "sensor-values").child("farm-irrigation-time").get().val()
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    print(current_time)
    if current_time == timeForIrrigation:
        print("Hello")
    sleep(1)
