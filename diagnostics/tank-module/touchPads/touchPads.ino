/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: touchPads.ino
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller: Atmega 328p
 * Pins used: Touch pads(5 nos):  A0,A1,A2,A3,A4
 * Purpose: Diagnose touch pads
 */

int touchPad1 = A0; // analog pin 0
int touchPad2 = A1; // analog pin 1
int touchPad3 = A2; // analog pin 2
int touchPad4 = A3; // analog pin 3
int touchPad5 = A4; // analog pin 4

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Touch pads (5 nos)
  pinMode(touchPad1, INPUT);
  pinMode(touchPad2, INPUT);
  pinMode(touchPad3, INPUT);
  pinMode(touchPad4, INPUT);
  pinMode(touchPad5, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int touchpadValue1 = analogRead(touchPad1); // Value of touchpad1
  int touchpadValue2 = analogRead(touchPad2); // Value of touchpad2
  int touchpadValue3 = analogRead(touchPad3); // Value of touchpad3
  int touchpadValue4 = analogRead(touchPad4); // Value of touchpad4
  int touchpadValue5 = analogRead(touchPad5); // Value of touchpad5
  int LEDCounter = 0; // Count the number of LED
  if (touchpadValue1 >= 1020) { // Checks if touch pad 1 is connected or not
    LEDCounter++;
  }
  if (touchpadValue2 >= 1020) { // Checks if touch pad 2 is connected or not
    LEDCounter++;
  }
  if (touchpadValue3 >= 1020) { // Checks if touch pad 3 is connected or not
    LEDCounter++;
  }
  if (touchpadValue4 >= 1020) { // Checks if touch pad 4 is connected or not
    LEDCounter++;
  }
  if (touchpadValue5 >= 1020) { // Checks if touch pad 5 is connected or not
    LEDCounter++;
  }
  Serial.println(LEDCounter);
  delay(500);
}
