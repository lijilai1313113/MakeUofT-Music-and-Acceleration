#Libraries
import RPi.GPIO as GPIO
import time
from time import sleep
#Disable warnings (optional)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
triggerpin = 17 
GPIO.setup(triggerpin,GPIO.OUT)
#Run forever loop
#buzzer.changeFrequency(1000)
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

    while time.time() < t_end:
        buzzer.start(freqCycle)
    buzzer.stop()



