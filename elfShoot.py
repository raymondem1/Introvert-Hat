import time
import serial
from playsound import playsound

ser = serial.Serial('COM5', 9600)

time.sleep(5)

def play():
    playsound('elf2.wav')
    ser.write(b'H')
    time.sleep(2)

#ser.read()
play()