// includes
#include "CmdMessenger.h"

// Defines
#define BAUD_RATE 115200
#define mockWireless Serial2

// Possible rocket command list
enum {
  start_initialisation = 0,
  skip_gps = 1,
  begin_loop = 2,
};

// Define list of possible commands
enum {
    get_rocket_location,
    rocket_location_response,
    send_rocket_command,
    rocket_command_response,
    rocket_acknowledge_command,
    rocket_init_info,
    error,
};

// Defines possible rocket states
enum {
  pre_init,
  initialising,
  gps_locking,
  ready,
  running,
};

// Holds string which contains Initialisation information
String responseBuffer;

int state = pre_init;

// Create CmdMessenger instance
CmdMessenger messenger = CmdMessenger(Serial);

/* Set up messenger callbacks */

void on_get_rocket_location(void) {
    messenger.sendCmd(rocket_location_response, "41/.432/,13/.541");
}

void on_send_rocket_command(void) {
    int value1 = messenger.readBinArg<int>();
    switch (value1) {
      case start_initialisation:
        sendMockSerial("start");
        if (acknowledged()) {
          messenger.sendCmd(rocket_acknowledge_command, "Initialisation started");
          state = initialising;
        }
        break;
      case skip_gps:
        sendMockSerial("skip_gps");
        if (acknowledged()) {
          messenger.sendCmd(rocket_acknowledge_command, "GPS skipped");
          state = ready;
        }
        break;
      case begin_loop:
        sendMockSerial("begin");
        if (acknowledged()) {
          messenger.sendCmd(rocket_acknowledge_command, "Main loop begin");
        }
        break;
      default:
        messenger.sendCmd(error, "Command not recognised");
        break;
    }
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
    mockWireless.begin(BAUD_RATE);
    attach_callbacks();
}

void loop() {
    messenger.feedinSerialData();

    if (state == initialising || state == gps_locking) {
      feedinInitSerialData();
    }
}

// Presentation mock functions
void feedinInitSerialData() {
  if (mockWireless.available()) {
    char rec = mockWireless.read();
    if (String(rec) == ";") {

      if (responseBuffer == "GPS_LOCK") {
        state = gps_locking;
      } else if (responseBuffer == "GPS_OK") {
        state = ready;
      }

      messenger.sendCmd(rocket_init_info, responseBuffer);
      responseBuffer = "";
    } else {
      responseBuffer += String(rec);
    }
  }
}

boolean acknowledged() {
  String res = waitMockResponse();
  return (res == "ok");
}

void sendMockSerial(String message) {
  // Block until serial ready
  while (!mockWireless.available());

  mockWireless.println(message);
}

String waitMockResponse() {
  // Block until command recieved
  while (!mockWireless.available());

  String recieved;
  boolean stringComplete = false;
  while (!stringComplete) {
    // Only try read a char if it's available
    if (mockWireless.available()) {
       char recChar = mockWireless.read();
       if (String(recChar) == "\n" || String(recChar) == "\r") {
          stringComplete = true;
        } else {
          recieved += String(recChar);
        }
    }
  }

  // Clear out what's left in the buffer
  flushSerialBuffer();

  return recieved;
}

// Stupid hack to clear out any remaining character
void flushSerialBuffer() {
  while (mockWireless.available()) {
    char z = mockWireless.read();
  }
}
