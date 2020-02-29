import serial
import csv

ser = serial.Serial('COM3', baudrate = 9600)

while 1:
    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
