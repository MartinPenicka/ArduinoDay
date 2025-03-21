from machine import Pin
import utime

pins = [2,3,4,5,6,7,8,9]
leds = []

counter = 0

def button_click(pin):
    global counter
    
    counter += 1
    print(f"Counter is {counter}")

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_click)

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))

duration = 0.5

def blink_all(dur):
    
    for led in leds:
        led.value(1)
        
    utime.sleep(dur)
    
    for led in leds:
        led.value(0)

    utime.sleep(dur)
    
def blink_single_left(dur):
    
    for led in leds:
        led.value(0)
        utime.sleep(dur)
        led.value(1)
        utime.sleep(dur)

while True:
    
    blink_single_left(duration)
        
    #utime.sleep(1)
        