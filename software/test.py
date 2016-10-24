import PyCmdMessenger

# Initialize an ArduinoBoard instance.  This is where you specify baud rate and
# serial timeout.  If you are using a non ATmega328 board, you might also need
# to set the data sizes (bytes for integers, longs, floats, and doubles).
arduino = PyCmdMessenger.ArduinoBoard("/dev/cu.usbmodem1956731",baud_rate=9600)

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.
commands = [["rocket_location",""],
            ["rocket_location_is","s"],
            ["send_rocket_command","i"],
            ["rocket_command_response","s"],
            ["error","s"]]

# Initialize the messenger
c = PyCmdMessenger.CmdMessenger(arduino,commands)

# Send
c.send("current_location")
msg = c.receive()
print(msg)

# Send with multiple parameters
c.send("send_rocket_command", 1)
msg = c.receive()
print(msg)
