import pyrebase  # python library for firebase
config = {  # configuration for connection
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com",
}
firebase = pyrebase.initialize_app(config)  # firebase connection object
db = firebase.database()  # firebase database initialisation

# To create and update values in db
db.child("sensor-values").update(
    {"water-tank-percentage": "70",
     "pump-status": "false",
     "moisure-percentage": "50",
     "garden-valve": "false",
     "tank-valve": "false",
     "any-valve-open": "false"})

# users = db.child("sensor-values").child("Moisure percentage").get()

# print(users.val())
