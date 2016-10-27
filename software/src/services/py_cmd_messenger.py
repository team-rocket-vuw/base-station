import PyCmdMessenger
import threading
import time

SERIAL_PORT = "/dev/cu.usbmodem2129351"
BAUD_RATE = 115200

ARDUINO_INTERFACE = PyCmdMessenger.ArduinoBoard(SERIAL_PORT, baud_rate = BAUD_RATE)

MESSENGER_COMMANDS = [
                        ["get_rocket_location",""],
                        ["rocket_location_response","s"],
                        ["send_rocket_command","i"],
                        ["rocket_command_response","s"],
                        ["rocket_acknowledge_command", "s"],
                        ["rocket_init_info", "s"],
                        ["error","s"]
                    ]

MESSENGER = PyCmdMessenger.CmdMessenger(ARDUINO_INTERFACE, MESSENGER_COMMANDS)

class PyCmdMessenger(threading.Thread):
    def __init__(self, threadID, name, server):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.server = server

    def send_start_command(self):
        MESSENGER.send("send_rocket_command", 0)
        response = MESSENGER.receive()
        return response

    def send_skip_command(self):
        MESSENGER.send("send_rocket_command", 1)
        response = MESSENGER.receive()
        return response

    def send_begin_command(self):
        MESSENGER.send("send_rocket_command", 2)
        response = MESSENGER.receive()
        return response

    def run(self):
        while True:
            MESSENGER.send("get_rocket_state_info")
            response = MESSENGER.receive()

