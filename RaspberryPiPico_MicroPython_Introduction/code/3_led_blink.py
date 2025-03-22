'''
Blika nekolika LED
'''
from machine import Pin
import utime

led1 = Pin(2, Pin.OUT)
led2 = Pin(3, Pin.OUT)
led3 = Pin(4, Pin.OUT)

duration = 0.5

while True:
    
    led1.value(0)
    utime.sleep(duration)
    led1.value(1)
    led2.value(0)
    utime.sleep(duration)
    led2.value(1)
    led3.value(0)
    utime.sleep(duration)
    led3.value(1)
