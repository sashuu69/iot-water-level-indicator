/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: i2cserialSend.ino
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Nov 2019
 * Microcontroller : Atmega 328p
 * Purpose : Diagnose serial sending
 */

// Header files
#include <Wire.h> // For serial communication
#define SLAVE_ADDRESS 0x05 // Slave address for valve control
 
void setup() {
  // put your setup code here, to run once:
  Wire.begin(SLAVE_ADDRESS);
}

void loop() {
  // put your main code here, to run repeatedly:
  Wire.write("*");
  Wire.write("ttss");
  Wire.write("#");
  Wire.write("qqww");
}
