/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : i2cReceive.ino
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Nov 2019
 * Microcontroller : Atmega 328p
 * Purpose : Diagnose I2C receive
 */

// Header files
#include <Wire.h> // For serial communication
#define SLAVE_ADDRESS 0x04 // Slave address for valve control

char valveControlReceiveValue[10];

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i = 0;
  int valveNum;
  while (Wire.available()) { // To run in loop
    valveControlReceiveValue[i] = Wire.read(); // Read from serial communication
    i++;
    Serial.print(".");
  }
  Serial.println("Getting from I2C..");
  valveControlReceiveValue[i] = '\0';
  valveNum = valveControlReceiveValue - '0'; // Convert character number to digit
  Serial.println(valveNum);
}
