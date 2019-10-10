/*
 * Projecr Name : IOT based water level indicator
 * Project repository link : https://github.com/sashuu6/CET-MCA-S5-MiniProject-IOT_based_Water_Level_Indicator
 * Author : Sashwat K
 * Created on : 10 Oct 2019
 * Last updated : 10 Oct 2019
 * Microcontroller: Atmega 328p
 * Pins used: Ultrasonic sensor:  Trigger pin - 4
 *                                echo pin - 5
 *            Touch pads(5 nos):  6,7,8,9,10
 */

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
            long DetectWaterLevel();
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
long waterLevelUltrasonicSensor() {
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonicSensorTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonicSensorTriggerPin, LOW);
  durationForPulse = pulseIn(ultasonicSensorEchoPin, HIGH);
  waterLevelDistance = microsecondsToCentimeters(duration);
//  Serial.print("Water level (CM): ");
//  Serial.println(waterLevelDistance);
  return waterLevelDistance;
}

waterLevelDetection waterLevel;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  waterLevel.ultraSonicInitialisation();
}

void loop() {
  // put your main code here, to run repeatedly:
  waerLevel.waterLevelUltrasonicSensor();

}
