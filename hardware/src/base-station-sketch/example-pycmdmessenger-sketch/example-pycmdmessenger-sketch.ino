/*
  TODO Needs to be integrated with metis-2 code
*/

#include "CmdMessenger.h"

/* Define available CmdMessenger commands */
enum {
    rocket_location,
    rocket_location_is,
    send_rocket_command,
    rocket_command_response,
    error,
};

/* Initialize CmdMessenger -- this should match PyCmdMessenger instance */
const int BAUD_RATE = 9600;
CmdMessenger c = CmdMessenger(Serial);

/* Create callback functions to deal with incoming messages */

/* callback */
void on_rocket_location(void){
    c.sendBinCmd(rocket_location_is, "51.412");
}

/* callback */
void on_send_rocket_command(void){

    /* Grab two integers */
    int command = c.readBinArg<int>();

    /* Send result back */
    c.sendBinCmd(rocket_command_response, command);

}

/* callback */
void on_unknown_command(void){
    c.sendCmd(error,"Command without callback.");
}

/* Attach callbacks for CmdMessenger commands */
void attach_callbacks(void) {
    c.attach(rocket_location, on_rocket_location);
    c.attach(send_rocket_command, on_send_rocket_command);
    c.attach(on_unknown_command);
}

void setup() {
    Serial.begin(BAUD_RATE);
    attach_callbacks();
}

void loop() {
    c.feedinSerialData();
}
