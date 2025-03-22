'''
Po stisku tlacitka se rozsviti LED
'''
from machine import Pin
import time

led = Pin(2, Pin.OUT)

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.2)