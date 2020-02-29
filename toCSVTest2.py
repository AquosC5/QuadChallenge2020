import serial
import csv
import time

f = open("arduinoRandom.csv", "w")

f.write("Start\n")

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)

count = 0

time.sleep(2) #fixes launch problem, keeps data, but I do not like this method


while count < 20:
    arduinoData = ser.readline().decode('ascii') #on launch, ser does not have output anything on first iteration
    print(arduinoData)
    f.write(arduinoData)
    count+=1

f.close()


