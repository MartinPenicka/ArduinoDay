from machine import Pin
import time

leds = [4, 5, 6]

for led in leds:
    leds.append(Pin(led, Pin.OUT))

duration = 0.5

while True:
    
    for led in leds:
        led.value(1)
        time.sleep(duration)
        led.value(0)
        time.sleep(duration)
