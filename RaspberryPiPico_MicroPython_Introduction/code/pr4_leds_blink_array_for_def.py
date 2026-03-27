'''
Blika nekolika LED, je pouzito pole, for cyklis a definice funkce
'''
from machine import Pin
import time

pins = [2, 3, 4]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))
    
def blink(dur):
    for led in leds:
        led.value(0)
        time.sleep(dur)
        led.value(1)
        time.sleep(dur)

while True:
    
    blink(0.5)