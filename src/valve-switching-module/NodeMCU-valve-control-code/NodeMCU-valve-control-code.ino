/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: NodeMCU-valve-control-code.ino
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 10 Oct 2019
 * Microcontroller: Atmega 328p
 * Pins used: solenoid valve 1: 4
 *            solenoid valve 2: 5
 *            solenoid valve 3: 6
 */

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
  }
}

solenoidValue SV; // class SolenoidValve's object

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SV.initialiseTankModule();
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(1);
}
