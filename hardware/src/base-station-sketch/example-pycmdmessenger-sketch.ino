/*
  Example sketch utilising PyCmdMessenger Library

  This sketch contains several basic use cases of the PyCmdMessenger
  library.

  TODO Requires full compatiability testing once hardware base station is complete.

  Created 7 September 2016
  By Marcel van Workum

  Modified 7 September 2016
  By Marcel van Workum
*/

#include "CmdMessenger.h"

/* Define available CmdMessenger commands */
enum {
    current_location,
    current_location_is,
    send_rocket_command,
    rocket_command_response,
    error,
};

/* Initialize CmdMessenger -- this should match PyCmdMessenger instance */
const int BAUD_RATE = 9600;
CmdMessenger c = CmdMessenger(Serial);

/* Create callback functions to deal with incoming messages */

/* callback */
void on_current_location(void){
    c.sendCmd(current_location_is, "Developing");
}

/* callback */
void on_send_rocket_command(void){

    /* Grab two integers */
    int command = c.readBinArg<int>();
    int options = c.readBinArg<int>();

    // Do command logic

    /* Send result back */
    c.sendBinCmd(rocket_command_response, "Command response message");

}

/* callback */
void on_unknown_command(void){
    c.sendCmd(error,"Command without callback.");
}

/* Attach callbacks for CmdMessenger commands */
void attach_callbacks(void) {
    c.attach(current_location, on_current_location);
    c.attach(send_rocket_command, on_send_rocket_command);
    c.attach(on_unknown_command);
}

void setup() {
    Serial.begin(BAUD_RATE);
    attach_callbacks();
}

void loop() {
    c.feedinSerialData();
    delay(500);
}
