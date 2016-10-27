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
    get_rocket_state_info,
    rocket_init_state_response,
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

enum {
  component_pre_init,
  component_success,
  component_fail,
};

// Holds string which contains Initialisation information
String responseBuffer = "";
String status = "";
String info = "";

// Component state info
int dmState = component_pre_init;
int rfmState = component_pre_init;

String gps_state = "waiting";
String gps_vis = "Uninitialised";
String gps_lat = "Uninitialised";
String gps_lng = "Uninitialised";

int state = pre_init;

// Create CmdMessenger instance
CmdMessenger messenger = CmdMessenger(Serial);

/* Set up messenger callbacks */

void on_get_rocket_location(void) {
    messenger.sendCmd(rocket_location_response, "41/.432/,13/.541");
}

void on_get_rocket_state_info(void) {
    messenger.sendCmd(rocket_init_state_response, info);
}

void on_send_rocket_command(void) {
    int value1 = messenger.readBinArg<int>();
    switch (value1) {
      case start_initialisation:
        sendMockSerial("start");
        if (acknowledged()) {
          messenger.sendCmd(rocket_command_response, "Initialisation started");
          state = initialising;
        }
        break;
      case skip_gps:
        sendMockSerial("skip_gps");
        if (acknowledged()) {
          messenger.sendCmd(rocket_command_response, "GPS skipped");
          state = ready;
        }
        break;
      case begin_loop:
        sendMockSerial("begin");
        if (acknowledged()) {
          messenger.sendCmd(rocket_command_response, "Main loop begin");
        }
        break;
      default:
        messenger.sendCmd(rocket_command_response, "Command not recognised");
        break;
    }
}

void on_unknown_command(void) {
    messenger.sendCmd(error,"Command without callback.");
}

// Attach the callbacks
void attach_callbacks(void) {
    messenger.attach(get_rocket_location, on_get_rocket_location);
    messenger.attach(get_rocket_state_info, on_get_rocket_state_info);
    messenger.attach(send_rocket_command, on_send_rocket_command);
    messenger.attach(on_unknown_command);
}

void setup() {
    Serial.begin(BAUD_RATE);
    mockWireless.begin(BAUD_RATE);
    attach_callbacks();
    updateState();
}

void loop() {
    messenger.feedinSerialData();

    if (state == initialising || state == gps_locking) {
      feedinInitSerialData();
    }
}

// Presentation mock functions
void feedinInitSerialData() {
  boolean isPostEquals = false;
  if (mockWireless.available()) {
    char rec = mockWireless.read();
    if (String(rec) == ";") {
      updateState();
    } else if (String(rec) == "=") {
      isPostEquals = true;
    } else {
      if (isPostEquals) {
        responseBuffer += String(rec);
      } else {
        status += String(rec);
      }
    }
  }
}

void updateState() {
  if (responseBuffer == "DM") {
    int stateUpdate = (status == "OK") ? component_success : component_fail;
    dmState= stateUpdate;
  } else if (responseBuffer == "RFM") {
    int stateUpdate = (status == "OK") ? component_success : component_fail;
    rfmState = stateUpdate;
  } else if (responseBuffer == "GPS") {
    gps_state = status;
  } else if (responseBuffer == "GPSVIS") {
    gps_vis = status;
  } else if (responseBuffer == "GPSLAT") {
    gps_state = "ready";
    gps_lat = status;
  } else if (responseBuffer == "GPSLNG") {
    gps_state = "ready";
    gps_lng = status;
  }

  // Clear fields at this point
  responseBuffer = "";
  status = "";

  info = "{\n";

  info += "init_info: {\n";
  info += "DM: " + getStateName(dmState);
  info += "RFM: " + getStateName(rfmState);
  info += "},\n";

  info = "gps_info: {\n";
  info += "READY: " + gps_state + ",\n";
  info += "VIS: " + gps_vis + ",\n";
  info += "LAT: " + gps_lat + ",\n";
  info += "LNG: " + gps_lng + ",\n";
  info += "},\n";

  info += "}";
}

String getStateName(int componentState) {
  switch (componentState) {
    case component_pre_init:
      return "\"waiting\",\n";
      break;
    case component_success:
      return "\"True\",\n";
      break;
    case component_fail:
      return "\"False\",\n";
      break;
    default:
      return "\"Not recognised\",\n";
      break;
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
