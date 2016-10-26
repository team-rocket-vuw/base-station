// includes
#include "CmdMessenger.h"

// Defines
#define BAUD_RATE 9600;

// Define list of possible commands
enum {
    get_rocket_location,
    rocket_location_response,
    send_rocket_command,
    rocket_command_response,
    error,
};

// Create CmdMessenger instance
CmdMessenger messenger = CmdMessenger(Serial);

/* Set up messenger callbacks */

void on_get_rocket_location(void) {
    messenger.sendCmd(rocket_location_response, "41/.432/,13/.541");
}

void on_send_rocket_command(void) {
    int value1 = messenger.readBinArg<int>();
    messenger.sendBinCmd(rocket_command_response, value1);
}

void on_unknown_command(void) {
    messenger.sendCmd(error,"Command without callback.");
}

// Attach the callbacks
void attach_callbacks(void) {
    messenger.attach(get_rocket_location, on_get_rocket_location);
    messenger.attach(send_rocket_command, on_send_rocket_command);
    messenger.attach(on_unknown_command);
}

void setup() {
    Serial.begin(BAUD_RATE);
    attach_callbacks();
}

void loop() {
    messenger.feedinSerialData();
}
