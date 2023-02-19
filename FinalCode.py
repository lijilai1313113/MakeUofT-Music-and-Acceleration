import os
import sys
import time
from time import sleep
import smbus
import RPi.GPIO as GPIO


from imusensor.MPU9250 import MPU9250
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

triggerpin=17 
GPIO.setup(triggerpin,GPIO.OUT)
address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()

buzzer = GPIO.PWM(triggerpin, 784)
duration = 0.5
freqCycle = 1

c = 2093
d = 2300.32
e = 2537.02
f = 2793.83
g = 3135.96
a = 3520.7
b = 3900.07
c8 = 4186.01


def playNote(freq):
    buzzer.ChangeFrequency(freq)
    t_end = time.time() + duration
    print(freq)
    
    while time.time() < t_end:
        buzzer.start(freqCycle)
    buzzer.stop()

while True:
    imu.readSensor()
    imu.computeOrientation()
    print (imu.AccelVals[1])
    
    if abs(imu.AccelVals[1]) > 4.5*2:
        playNote(c8)
    elif abs(imu.AccelVals[1]) > 4*2:
        playNote(b)
    elif abs(imu.AccelVals[1]) > 3.5*2:
        playNote(a)
    elif abs(imu.AccelVals[1]) > 3*2:
        playNote(g)
    elif abs(imu.AccelVals[1]) > 2.5*2:
        playNote(f)
    elif abs(imu.AccelVals[1]) > 2*2:
        playNote(e)
    elif abs(imu.AccelVals[1]) > 1.5*2:
        playNote(d)
    elif abs(imu.AccelVals[1]) > 1*2:
        playNote(c)
    else:
        continue
    
