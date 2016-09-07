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
    current_status,
    status_is,
    think_for_me,
    thought_is,
    error,
};

/* Initialize CmdMessenger -- this should match PyCmdMessenger instance */
const int BAUD_RATE = 9600;
CmdMessenger c = CmdMessenger(Serial);

/* Create callback functions to deal with incoming messages */

/* callback */
void on_current_status(void){
    c.sendCmd(status_is,"Developing");
}

/* callback */
void on_think_for_me(void){

    /* Grab two integers */
    int value1 = c.readBinArg<int>();
    int value2 = c.readBinArg<int>();

    /* Send result back */
    c.sendBinCmd(thought_is,value1 * value2);

}

/* callback */
void on_unknown_command(void){
    c.sendCmd(error,"Command without callback.");
}

/* Attach callbacks for CmdMessenger commands */
void attach_callbacks(void) {
    c.attach(current_status,on_current_status);
    c.attach(think_for_me,on_think_for_me);
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
