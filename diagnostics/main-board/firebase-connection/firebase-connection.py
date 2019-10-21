from firebase import Firebase

config = {
    "apiKey": "AIzaSyB7lLBSm2O9p0y4ZuH5umbr0OMikKDJ0bs",
    "authDomain": "miniproject-iot-water.firebaseapp.com",
    "databaseURL": "https://miniproject-iot-water.firebaseio.com",
    "storageBucket": "miniproject-iot-water.appspot.com"
}

firebase = Firebase(config)

print(firebase)
