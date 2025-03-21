from machine import Pin
import time

led = Pin(4, Pin.OUT)

button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.2)