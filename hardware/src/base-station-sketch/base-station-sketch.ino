/*
  Basestation electronics sketch
  
  This sketch contains code to communicate with the rocket on the launch pad via 2.4GHz WiFi,
  and then allows communication over the 434MHz band post-launch
  This sketch is written for use on a Teensy 3.1/3.2
  
  The circuit: 
  * Components Used:
    - ESP8266-01 WiFi Module
      * TXD - pin 9
      * RXD - pin 10
    - RFM22B-S2 434MHz radio tranciever
      * SDI    - pin 11
      * SDO    - pin 12
      * CLK    - pin 13
      * CS     - as defined in radioChipSelect field
      
  Created 28 August 2016
  By Jamie Sanson
  
  Modified 28 August 2016
  By Jamie Sanson
  
*/

// region includes
#include <ESP8266.h>
// end region

// region macro definitions
#define espSerial Serial2
#define serialBaud 115200
#define espSerialBaud 9600
// end region

// region pin definitions
int8_t radioChipSelect = 5;
int8_t radioIntPin = 15;
// end region

// region flags
boolean serialDebugMode = true;
// end region

// region library instantiation
ESP8266 wifi(espSerial);
// end region

void setup() {
  if (serialDebugMode) {
    Serial.begin(serialBaud);

    // block until serial sent to teensy
    while (!Serial.available());
  }
  
  // TODO: Radio initialisation and WiFi connection
}

void loop() {
  // TODO: WiFi & Serial listening and cmd forwarding
}
