import PyCmdMessenger
import threading
import time

SERIAL_PORT = "/dev/cu.usbmodem1411"
BAUD_RATE = 9600

ARDUINO_INTERFACE = PyCmdMessenger.ArduinoBoard(SERIAL_PORT, baud_rate = BAUD_RATE)

MESSENGER_COMMANDS= [["rocket_location",""],
                    ["rocket_location_is","s"],
                    ["send_rocket_command","i"],
                    ["rocket_command_response","s"],
                    ["error","s"]]

MESSENGER = PyCmdMessenger.CmdMessenger(ARDUINO_INTERFACE, MESSENGER_COMMANDS)

class PyCmdMessenger(threading.Thread):
    def __init__(self, threadID, name, server):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.server = server

    def run(self):
        while True:
            MESSENGER.send("rocket_location")
            response = MESSENGER.receive()
            location = response[1][0]
            formatted_string = location.replace("/.", ".").split(",")
            formatted_location = list(map(float, formatted_string))
            self.server.lat = formatted_location[0]
            self.server.lng = formatted_location[1]
