'''
Blikani nekolika LED pomoci pole a cyklu
'''
from machine import Pin
import utime

pins = [2, 3, 4]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))

duration = 0.5

while True:
    
    for led in leds:
        led.value(0)
        utime.sleep(duration)
        led.value(1)
        utime.sleep(duration)