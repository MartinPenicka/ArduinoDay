'''
Po stisku tlacitka se rozsviti LED, po uvolneni tlacitka zhasne
'''
from machine import Pin
import time

led = Pin(2, Pin.OUT)

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    
    if button.value() == 0:
        led.value(0)
    else:
        led.value(1)
    time.sleep(0.2)