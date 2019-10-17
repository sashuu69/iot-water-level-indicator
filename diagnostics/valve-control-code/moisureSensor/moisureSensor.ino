/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: NodeMCU-valve-control-code.ino
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller : Atmega 328p
 * Pins used: Moisure sensor: A0
 * Purpose: Diagnose moisure sensor testing
 */

 int moisureSensorPin = A0;
 int moisurePercentage;
 
void setup() {
  // put your setup code here, to run once:
  pinMode(moisureSensorPin,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  moisurePercentage = analogRead(moisureSensorPin);
  moisurePercentage = map(moisurePercentage,550,0,0,100);
  Serial.print("Moisure Percentage: ");Serial.print(moisurePercentage);Serial.println(" %");
}
