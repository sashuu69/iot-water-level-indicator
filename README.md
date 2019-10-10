# IOT Based Water Level Indicator

## Introduction

The IOT based Water Level Indicator is the mini project under MCA course. The user can get water level through mobile app and web interface.

## Features

1. Realtime water level, pump status and value status.
2. Web interface and android app.
3. manual remote control pump control.
4. Automatic sprinker system according to moisure content.
5. OLED display for showing status.

## Hardware modules

1. Main board module.
2. Water tank module.
3. valve switching module.

### Main board Module Components

1. Raspberry Pi Zero W
2. Relay (220V - 5V)

### Water Tank Module Components

1. Touch pads - 5
2. Ultrasonic sensor - 1
3. Atmega328p

### Valve Switching Components

1. Solenoid valve - 3
2. Atmega328p

Notes:-

1. The communication between the modules is via serial communication.
2. All the data is stored in firebase.

## Files and folders explained

### Folders

1. abstract: contains the project abstract.
2. Diagrams: contains important figures drawn using draw.io.
3. Zeroth-review-presentation: contains presentation done for zeroth review.
4. first-review: contains user stories submitted in first review.
5. src - Contains the source code.
   1. android-app: contains the code for android app.
   2. main-board-module: contains code for Raspberry Pi Zero W.
   3. tank-module: contains embedded C code for Atmega328p. This micro-controller will be placed at water Tank.
   4. valve-switching-module: conatins embedded C code for ATmega328p. This micro-controller will be placed at the main pipeline junction.
