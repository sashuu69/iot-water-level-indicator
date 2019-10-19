/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: arduino-valve-control-code.ino
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 17 Oct 2019
 * Microcontroller : Atmega 328p
 * Pins used: solenoid valve 1: 4
 *            solenoid valve 2: 5
 *            solenoid valve 3: 6
 *            Moisure sensor: A0
 */
 
// Header files
#include <Wire.h> // For I2C communication
#define SLAVE_ADDRESS 0x04 // Slave address for valve control

/*************************************************/
/*************************************************/
// Class defined to handle water Level in the tank
/*************************************************/
/*************************************************/
class solenoidValue {
  private:
            int tankSolenoidValve = 4;
            int sprinklerSolenoidValve = 5;
            int farmSolenoidValve = 6;
  public:
            void initialiseTankModule(); // Function to initilase the solenoid pins
            void solenoidSwitchTrigger(int); // Function to trigger the solenoid valve
};

/*******************************************/
// Function to initialize the solenoid pins 
/*******************************************/
void solenoidValue::initialiseTankModule() {
  pinMode(tankSolenoidValve, OUTPUT);
  pinMode(sprinklerSolenoidValve, OUTPUT);
  pinMode(farmSolenoidValve, OUTPUT);
}

/**************************************/
// Function to trigger a solenoid valve
/**************************************/
void solenoidValue::solenoidSwitchTrigger(int valveTag) {
  if (valveTag == 1) {
    digitalWrite(tankSolenoidValve, HIGH);
    digitalWrite(sprinklerSolenoidValve, LOW);
    digitalWrite(farmSolenoidValve, LOW);
    Serial.print("Tank valve ON ");
    Serial.print("Sprinkler valve OFF ");
    Serial.println("Farm valve OFF ");
  }
  else if (valveTag == 2) {
    digitalWrite(tankSolenoidValve, LOW);
    digitalWrite(sprinklerSolenoidValve, HIGH);
    digitalWrite(farmSolenoidValve, LOW);
    Serial.print("Tank valve OFF ");
    Serial.print("Sprinkler valve ON ");
    Serial.println("Farm valve OFF ");
  }
  else if (valveTag == 3) {
    digitalWrite(tankSolenoidValve, LOW);
    digitalWrite(sprinklerSolenoidValve, LOW);
    digitalWrite(farmSolenoidValve, HIGH);
    Serial.print("Tank valve OFF ");
    Serial.print("Sprinkler valve OFF ");
    Serial.println("Farm valve ON ");
  }
  else {
    digitalWrite(tankSolenoidValve, LOW);
    digitalWrite(sprinklerSolenoidValve, LOW);
    digitalWrite(farmSolenoidValve, LOW);
    Serial.print("Wrong valveTag value: ");
    Serial.println(valveTag);
  }
}

/************************************************************/
/************************************************************/
// Class defined to handle moisure sensor present in the soil
/************************************************************/
/************************************************************/
class MosiureLevel {
  private:
            int moisureSensorPin = A0;
            int moisurePercentage;
  public:
            void InitialiseMoisureSensor();
            int MoisturePercentage();
};

/***************************************/
// Function to initialise moisure sensor
/***************************************/
void MosiureLevel::InitialiseMoisureSensor() {
  pinMode(moisureSensorPin,INPUT);
}

/*******************************************/
// Function to get moisture level precentage
/*******************************************/
int MosiureLevel::MoisturePercentage() {
  moisurePercentage = analogRead(moisureSensorPin);
  moisurePercentage = map(moisurePercentage,550,0,0,100);
  return moisurePercentage;
}

solenoidValue SV; // class SolenoidValve's object
MosiureLevel ML; // class MosiureLevel's object

int MPer;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Serial.println("Arduino Valve Control Code:-");
  SV.initialiseTankModule();
  ML.InitialiseMoisureSensor();
  Wire.onRequest(sendValue);
  Wire.onReceive(receiveEvent);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Moisure level
  MPer = ML.MoisturePercentage();
  Serial.print("Moisure Level: ");Serial.print(MPer);Serial.println(" %");
  Serial.println("--------------------------------");
//  delay(1000);
}

void sendValue() {
    Wire.write(MPer);
    Serial.println("Sending mosiure percentage through I2C");
}

void receiveEvent() {
  int lastRequest = Wire.read();
  Serial.println("Reading data  from I2C.");
  SV.solenoidSwitchTrigger(lastRequest);
}
