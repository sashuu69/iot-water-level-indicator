/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * File name: NodeMCU-tank-code.ino
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 10 Oct 2019
 * Microcontroller: Atmega 328p
 * Pins used: Ultrasonic sensor:  Trigger pin - 4
 *                                echo pin - 5
 *            Touch pads(5 nos):  6,7,8,9,10
 */

// Header files
#include <Wire.h> // For serial communication
#define SLAVE_ADDRESS 0x05 // Slave address for valve control

/*************************************************/
/*************************************************/
// Class defined to handle water Level in the tank
/*************************************************/
/*************************************************/
class waterLevelDetection {
  private:
            int ultrasonicSensorTriggerPin = 4; // Ultrasonic sensor - trigger - digital pin 4
            int ultasonicSensorEchoPin = 5; // Ultrasonic sensor - echo - digital pin 5
            long durationForPulse; // Store duration from sending a pulse to receiving it
            long waterLevelDistance; // Stores the distance between water and sensor in cm
            // 5 touch pad pins
            int touchPad1 = 6; // digital pin 6
            int touchPad2 = 7; // digital pin 7
            int touchPad3 = 8; // digital pin 8
            int touchPad4 = 9; // digital pin 9
            int touchPad5 = 10; // digital pin 10
  public:
            void ultraSonicInitialisation(); // Function to initialise the pins
            long waterLevelUltrasonicSensor(); // Function returns the water to sensor distance in cm
            int touchPadCount(); // Function that outputs the number of touch pads touching the water
 };

/***************************************************/
// Function to initialise the sensor pins at setup()
/***************************************************/
void waterLevelDetection::ultraSonicInitialisation() {
  // Ultrasonic sensor
  pinMode(ultrasonicSensorTriggerPin, OUTPUT);
  pinMode(ultasonicSensorEchoPin, INPUT);
  // Touch pads (5 nos)
  pinMode(touchPad1, INPUT);
  pinMode(touchPad2, INPUT);
  pinMode(touchPad3, INPUT);
  pinMode(touchPad4, INPUT);
  pinMode(touchPad5, INPUT);
}

/********************************************************/
// Function to detect water level from ultrasonic sensor
/********************************************************/
long waterLevelDetection::waterLevelUltrasonicSensor() {
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicSensorTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  durationForPulse = pulseIn(ultasonicSensorEchoPin, HIGH);
  waterLevelDistance = durationForPulse / 29 / 2;
  return waterLevelDistance;
}

/**********************************************************/
// Function to give the count of sensors touching the water
/**********************************************************/
int waterLevelDetection::touchPadCount() {
  int touchpadValue1 = digitalRead(touchPad1); // Value of touchpad1
  int touchpadValue2 = digitalRead(touchPad2); // Value of touchpad2
  int touchpadValue3 = digitalRead(touchPad3); // Value of touchpad3
  int touchpadValue4 = digitalRead(touchPad4); // Value of touchpad4
  int touchpadValue5 = digitalRead(touchPad5); // Value of touchpad5
  int LEDCounter = 0; // Count the number of LED
  if (touchpadValue1) { // Checks if touch pad 1 is connected or not
    LEDCounter++;
  }
  if (touchpadValue2) { // Checks if touch pad 2 is connected or not
    LEDCounter++;
  }
  if (touchpadValue3) { // Checks if touch pad 3 is connected or not
    LEDCounter++;
  }
  if (touchpadValue4) { // Checks if touch pad 4 is connected or not
    LEDCounter++;
  }
  if (touchpadValue5) { // Checks if touch pad 5 is connected or not
    LEDCounter++;
  }
  return LEDCounter;
}

/**************************************************************************/
/**************************************************************************/
// Class defined to handle communication between the contorl-board and tank.
/**************************************************************************/
/**************************************************************************/
class serialCommunicationTank {
  private:
            char waterInfoSendValue[10]; // To send touch pad levels and ultrasonic sensor distance through serial communication
  public:
            void serialCommunicationChannelSetup();
            void serialSendWaterInfo(int,int);
};

/*********************************************/
// Function to initialize serial communication.
/*********************************************/
void serialCommunicationTank::serialCommunicationChannelSetup() {
  Wire.begin(SLAVE_ADDRESS); // Initialising Serial communication
}

/*******************************************************************************/
// Function to send touch pad count and ultrasonic sensor distance communication.
/*******************************************************************************/
void serialCommunicationTank::serialSendWaterInfo(int tpCount, int uSSDist) {
//  char conversionChar[10]; // Convert to char and concatinate into *tpCount#uSSDist
  char temp1,temp2;
  temp1 = tpCount + '0';
  temp2 = uSSDist+ '0';
  Wire.write("*");
  Wire.write(temp1);
  Wire.write("#");
  Wire.write(temp2);
}

waterLevelDetection waterLevel; // Class waterLevelDetection's object
serialCommunicationTank SC; // Class serialCommunicationTank's object

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  SC.serialCommunicationChannelSetup();
  waterLevel.ultraSonicInitialisation();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  // Ultrasonic sensor
  int WD = (int) waterLevel.waterLevelUltrasonicSensor();

  // Touch pads (5 nos)
  int TPC = waterLevel.touchPadCount();

  // Serial communicate water level
  SC.serialSendWaterInfo(TPC,WD);
}
