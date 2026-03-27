'''
Zakladni priklad - blika LED primo na desce
'''
from machine import Pin
import utime

# RPi Pico pin = 25, RPi Pico W pin = "LED"
led = Pin("LED", Pin.OUT)

while True:
    
    led.toggle()
    utime.sleep(1)