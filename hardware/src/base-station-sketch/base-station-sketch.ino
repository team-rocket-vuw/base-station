// includes
#include "CmdMessenger.h"

// Defines
#define BAUD_RATE 115200
#define rocketConnection Serial2

// Possible rocket command list
enum {
  start_initialisation = 0,
  skip_gps = 1,
  begin_loop = 2,
};

// Define list of possible commands sent from pyCommandMessenger,
// as well as responses
enum {
  send_rocket_command,
  rocket_command_response,
  get_rocket_state_info,
  rocket_state_response,
  error,
};

// Defines possible rocket states, changed by data fed back via rocket connection
enum {
  pre_init,
  initialising,
  gps_locking,
  ready,
  running,
};

// Defines individual component state to be reported when rocket state is requested
enum {
  component_pre_init,
  component_success,
  component_fail,
};

// Holds string which contains Initialisation information
String state_type = "";
String status = "";
String info = "";

// Component state info
int dmState = component_pre_init;
int rfmState = component_pre_init;

String gps_state = "waiting";
String gps_vis = "Uninitialised";
String gps_lat = "Uninitialised";
String gps_lng = "Uninitialised";

// Overall rocket state
int state = pre_init;

// Used for feeding in rocket connection data
boolean isPostEquals = false;

// Create CmdMessenger instance
CmdMessenger messenger = CmdMessenger(Serial);

// --------------------- CALLBACKS ---------------------
void on_get_rocket_state_info(void) {
    messenger.sendCmd(rocket_state_response, info);
}

void on_send_rocket_command(void) {
    int value1 = messenger.readBinArg<int>();

    if (state == running) {
        messenger.sendCmd(rocket_command_response, "Main loop running");
        return;
    }

    switch (value1) {
      case start_initialisation:
        tryStartInitialisation();
        break;
      case skip_gps:
        trySkipGPSLock();
        break;
      case begin_loop:
        tryBeginLoop();
        break;
      default:
        messenger.sendCmd(rocket_command_response, "Command not recognised");
        break;
    }
}

void on_unknown_command(void) {
  messenger.sendCmd(error, "Command without callback.");
}

// Attach the callbacks
void attach_callbacks(void) {
    messenger.attach(get_rocket_state_info, on_get_rocket_state_info);
    messenger.attach(send_rocket_command, on_send_rocket_command);
    messenger.attach(on_unknown_command);
}

// --------------------- SETUP ---------------------
void setup() {
    Serial.begin(BAUD_RATE);
    rocketConnection.begin(BAUD_RATE);
    attach_callbacks();
    updateState();
}

// --------------------- LOOP ---------------------
void loop() {
  messenger.feedinSerialData();
  feedinStateData();
}

// -------- ROCKET COMMUNICATION FUNCTIONS ----------

/*
Function to be called when start initialisation command recieved. Checks state and
responds accordingly
*/
void tryStartInitialisation() {
  if (state == gps_locking) {
      sendMessage("start");
      if (acknowledged()) {
        messenger.sendCmd(rocket_command_response, "Initialisation started");
        state = initialising;
      }
  } else {
      messenger.sendCmd(rocket_command_response, "Rocket in incorrect state");
  }
}

/*
Function to be called when skip GPS command recieved. Checks state and
responds accordingly
*/
void trySkipGPSLock() {
  if (state == gps_locking) {
      sendMessage("skip_gps");
      if (acknowledged()) {
        messenger.sendCmd(rocket_command_response, "GPS skipped");
        state = ready;
      }
  } else {
      messenger.sendCmd(rocket_command_response, "Rocket in incorrect state");
  }
}

/*
Function to be called when begin loop command recieved. Checks state and
responds accordingly
*/
void tryBeginLoop() {
  if (state == ready) {
      sendMessage("begin");
      if (acknowledged()) {
        messenger.sendCmd(rocket_command_response, "Main loop started");
        state = running;
      }
  } else {
      messenger.sendCmd(rocket_command_response, "Rocket in incorrect state");
  }
}


/*
 Function to be called once per main loop iteration to feed in connection data to update rocket state.
 State messages are formatted as follows:
              GPSVIS=05;
 This message conveys GPS visibility information, where data is separated by an equals sign and
 concluded with a semicolon
*/
void feedinStateData() {
  if (rocketConnection.available()) {
    char rec = rocketConnection.read();
    if (String(rec) == ";") {
      updateState();
    } else if (String(rec) == "=") {
      isPostEquals = true;
    } else {
      if (!isPostEquals) {
        state_type += String(rec);
      } else {
        status += String(rec);
      }
    }
  }
}

/*
Function to be called when consuming of one message is complete, or once during setup. This builds a formatted
JSON hash containing two sub-hashes for easy parseability at the front-end, and stores it in the info field
to be accessed when get_rocket_state_info is called.
State types included:
    Initialisation information:
      DM: Data module initialisation
      RFM: RFM22b radio module initialisation
    GPS information:
      GPS: General GPS state
      GPSVIS: Visible satellites
      GPSLAT: GPS latitude readout
      GPSLNG: GPS longitude readout
*/
void updateState() {
  if (state_type == "DM") {
    int stateUpdate = (status == "OK") ? component_success : component_fail;
    dmState= stateUpdate;
  } else if (state_type == "RFM") {
    int stateUpdate = (status == "OK") ? component_success : component_fail;
    rfmState = stateUpdate;
  } else if (state_type == "GPS") {
    gps_state = status;
    if (gps_state == "locking") {
      state = gps_locking;
    }
  } else if (state_type == "GPSVIS") {
    gps_vis = status;
  } else if (state_type == "GPSLAT") {
    gps_state = "ready";
    gps_lat = status;
  } else if (state_type == "GPSLNG") {
    gps_state = "ready";
    gps_lng = status;
  }

  // Clear fields at this point
  state_type = "";
  status = "";
  isPostEquals = false;

  // Formatting state information into JSON hash
  info = "{";

  info += "'init_info': {";
  info += "'DM': " + getStateName(dmState, false);
  info += "'RFM': " + getStateName(rfmState, true);
  info += "}/,";

  info += "'gps_info': {";
  info += "'READY': '" + gps_state + "'/,";
  info += "'VIS': '" + gps_vis + "'/,";
  info += "'LAT': '" + gps_lat + "'/,";
  info += "'LNG': '" + gps_lng + "'";
  info += "}";

  info += "}";
}

/*
Function which takes a component state, enumerated at the top of the file and
whether or not this is the last field in the JSON hash/sub-hash to add commas
appropriately.
*/
String getStateName(int componentState, boolean last) {
  String toReturn = "";

  switch (componentState) {
    case component_pre_init:
      toReturn =  "'waiting'";
      break;
    case component_success:
      toReturn = "'True'";
      break;
    case component_fail:
      toReturn = "'False'";
      break;
    default:
      toReturn = "'Not recognised'";
      break;
  }

  return toReturn + (last ? "/," : "");
}

/*
Function which waits for an acknowledged response from the rocket
*/
boolean acknowledged() {
  String res = waitResponse();
  return (res == "ok");
}

/*
Function which sends a given message over the rocket connection
*/
void sendMessage(String message) {
  rocketConnection.println(message);
}

/*
Function which waits for information to be sent to the base station via the
rocket connection, strips newline and cariage returns and then flushes any
further incoming serial from the recieved buffer of the base station teensy
*/
String waitResponse() {
  // Block until command recieved
  while (!rocketConnection.available());

  String recieved;
  boolean stringComplete = false;
  while (!stringComplete) {
    // Only try read a char if it's available
    if (rocketConnection.available()) {
      // Read in a character
      char recChar = rocketConnection.read();
      // Complete the string if the read char is a line break, else concat onto the
      // recieved string
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
  while (rocketConnection.available()) {
      rocketConnection.read();
  }
}
