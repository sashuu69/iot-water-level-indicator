import pyrebase  # python library for firebase
config = {  # configuration for connection
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com",
}

firebase = pyrebase.initialize_app(config)  # firebase connection object
db = firebase.database()  # firebase database initialisation

# To create and update sensor-values table
db.child("sensor-values").update(
    {"water-tank-percentage": "70",
     "pump-status": "false",
     "moisure-percentage": "50",
     "garden-valve": "false",
     "tank-valve": "false",
     "any-valve-open": "false"}
)

# To create and update log table
db.child("log").child("2019/10/13").child("14:51:50").update(
    {"action": "Pump on"}
)

# To create and update users table
db.child("users").update(
    {"username": "vijitha",
     "password": "password"}
)

# TO get values from table
mosireValue = db.child("sensor-values").child("moisure-percentage").get()
print(mosireValue.val())
