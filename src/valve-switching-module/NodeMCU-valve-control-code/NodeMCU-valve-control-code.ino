/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: NodeMCU-valve-control-code.ino
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 10 Oct 2019
 * Microcontroller : Atmega 328p
 * Pins used: solenoid valve 1: 4
 *            solenoid valve 2: 5
 *            solenoid valve 3: 6
 *            Moisure sensor: A0
 */
 
 // Header files
#include <Wire.h> // For serial communication
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
    Serial.print("Tank valve ON");
    Serial.print("Sprinkler valve OFF");
    Serial.print("Farm valve OFF");
  }
  else if (valveTag == 2) {
    digitalWrite(tankSolenoidValve, LOW);
    digitalWrite(sprinklerSolenoidValve, HIGH);
    digitalWrite(farmSolenoidValve, LOW);
    Serial.print("Tank valve OFF");
    Serial.print("Sprinkler valve ON");
    Serial.print("Farm valve OFF");
  }
  else if (valveTag == 3) {
    digitalWrite(tankSolenoidValve, LOW);
    digitalWrite(sprinklerSolenoidValve, LOW);
    digitalWrite(farmSolenoidValve, HIGH);
    Serial.print("Tank valve OFF");
    Serial.print("Sprinkler valve OFF");
    Serial.print("Farm valve ON");
  }
  else {
    Serial.print("Wrong valveTag value. ");
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

/***********************************************************************************/
/***********************************************************************************/
// Class defined to handle communication between the contorl-board and valve control
/***********************************************************************************/
/***********************************************************************************/
class serialCommunicationValveControl {
  private:
            char valveControlReceiveValue[10]; // To get valve number to open solenoid valves from serial communication
            char moisureSensorSendValue[10]; // To send moisure sensor data through serial communication
  public:
            void serialCommunicationChannelSetup(); // Function to handle serial communication
            void serialSendMosiureData(int); // Function to send data through serial communication
            int serialReceiveValveData(); // Function to receive data through serial communication
};

/*********************************************/
// Function to initialize serial communication
/*********************************************/
void serialCommunicationValveControl::serialCommunicationChannelSetup() {
  Wire.begin(SLAVE_ADDRESS); // Initialising Serial communication
}


/************************************************************/
// Function to send moisure data through serial communication
/************************************************************/
void serialCommunicationValveControl::serialSendMosiureData(int valueToSnd) {
  char conversionChar; // Convert receiving integer data to character integer
  conversionChar = valueToSnd + '0'; // Convert digit to character number
  Wire.write(conversionChar);
}

/************************************************************/
// Function to receive valve number from serial communication
/************************************************************/
int serialCommunicationValveControl::serialReceiveValveData() {
  int i = 0;
  int valveNum;
  while (Wire.available()) { // To run in loop
    valveControlReceiveValue[i] = Wire.read(); // Read from serial communication
    i++;
  }
  valveControlReceiveValue[i] = '\0';
  valveNum = valveControlReceiveValue - '0'; // Convert character number to digit
  return valveNum;
}

solenoidValue SV; // class SolenoidValve's object
MosiureLevel ML; // class MosiureLevel's object
serialCommunicationValveControl SC; // class serialCommunicationValve's object

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SV.initialiseTankModule();
  ML.InitialiseMoisureSensor();
  SC.serialCommunicationChannelSetup();
}

void loop() {
  // put your main code here, to run repeatedly:

  // Serial communication for solenoid switch
  SV.solenoidSwitchTrigger(SC.serialReceiveValveData());
  
  // Moisure level
  ML.MoisturePercentage();
}
