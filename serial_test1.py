# -*- coding: utf-8 -*-
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

while True:
    var = raw_input()
    print("input>>" +var)
    if var == "x":
        break
    if var =="a":
        ser.write(b'a')
        print("A")
    if var =="b":
        ser.write(b'B')
        print("B")
print("end")
ser.close()

