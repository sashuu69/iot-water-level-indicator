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
            void initialiseTankModule();
}
