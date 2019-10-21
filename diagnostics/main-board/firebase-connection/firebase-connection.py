from pyrebase

config = {
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com"
}

firebase = pyrebase.initialize_app(config)

archer = {"name": "Sterling Archer", "agency": "Figgis Agency"}
db.child("agents").push(archer, user['idToken'])
