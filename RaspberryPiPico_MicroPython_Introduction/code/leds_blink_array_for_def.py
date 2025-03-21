from machine import Pin
import time

pins = [4, 5, 6]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))
    
def blink(dur):
    for led in leds:
        led.value(1)
        time.sleep(dur)
        led.value(0)
        time.sleep(dur)

while True:
    
    blink(0.5)