import serial
import time

ser = serial.Serial(
        port='COM4',\
        baudrate=9600,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

seq = []
count = 1

while True:
    for c in ser.read():
        seq.append(chr(c))
        joined_seq = ''.join(str(v) for v in seq)

        if chr(c) == '\n':
            print("Line " + str(count) + ': ' + joined_seq)
            seq = []
            count += 1
            break

ser.close()
