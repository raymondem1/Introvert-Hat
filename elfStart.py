import time
import serial
ser = serial.Serial('COM5', 9600)
from playsound import playsound

time.sleep(5)

def play():
    playsound('elf1.wav')
    ser.write(b'H')

#ser.read()
play()