/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name : solenoidValve.ino
 * Author : Sashwat K
 * Created on : 17 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller : Atmega 328p
 * Pins used : solenoid valve 1 - 4
 *             solenoid valve 2 - 5
 *             solenoid valve 3 - 6
 * Purpose : Diagnose solenoid valve testing
 */

int tankSolenoidValve = 4;
int sprinklerSolenoidValve = 5;
int farmSolenoidValve = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(tankSolenoidValve, OUTPUT);
  pinMode(sprinklerSolenoidValve, OUTPUT);
  pinMode(farmSolenoidValve, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(tankSolenoidValve, HIGH);
  digitalWrite(sprinklerSolenoidValve, LOW);
  digitalWrite(farmSolenoidValve, LOW);
  delay(2000);
  digitalWrite(tankSolenoidValve, LOW);
  digitalWrite(sprinklerSolenoidValve, HIGH);
  digitalWrite(farmSolenoidValve, LOW);
  delay(2000);
  digitalWrite(tankSolenoidValve, LOW);
  digitalWrite(sprinklerSolenoidValve, LOW);
  digitalWrite(farmSolenoidValve, HIGH);
  delay(2000);
}
