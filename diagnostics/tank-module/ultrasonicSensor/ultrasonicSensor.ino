/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: ultrasonicSensor.ino
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 10 Oct 2019
 * Microcontroller: Atmega 328p
 * Pins used: Ultrasonic sensor:  Trigger pin - 4
 *                                Echo pin - 5
 */

int ultrasonicSensorTriggerPin = 4; // Ultrasonic sensor - trigger - digital pin 4
int ultasonicSensorEchoPin = 5; // Ultrasonic sensor - echo - digital pin 5
long durationForPulse; // Store duration from sending a pulse to receiving it
long waterLevelDistance; // Stores the distance between water and sensor in cm

void setup() {
  // put your setup code here, to run once:
  // Ultrasonic sensor
  pinMode(ultrasonicSensorTriggerPin, OUTPUT);
  pinMode(ultasonicSensorEchoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicSensorTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  durationForPulse = pulseIn(ultasonicSensorEchoPin, HIGH);
  waterLevelDistance = durationForPulse / 29 / 2;
  Serial.print("Distance: ");Serial.println(waterLevelDistance);
}
