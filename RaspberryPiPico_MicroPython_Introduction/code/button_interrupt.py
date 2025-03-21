from machine import Pin
import utime

pins = [4, 5, 6]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))
    
mode = 0
counter = 0

last_click_time = 0
debounce_delay = 150
    
def button_click(pin):
    global mode, counter, last_click_time, debounce_delay
    
    curr_time = utime.ticks_ms()
    time_diff = utime.ticks_diff(curr_time, last_click_time)
    last_click_time = curr_time
    
    if time_diff < debounce_delay:
        return
    
    counter += 1
    print(f"Counter is {counter}")
    if mode == 0:
        mode = 1
        return
    mode = 0
    
button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_click)
    
def blink(dur, direction):
    
    if direction == 0:
        for led in leds:
            led.value(1)
            utime.sleep(dur)
            led.value(0)
            utime.sleep(dur)
    else:
        for led in reversed(leds):
            led.value(1)
            utime.sleep(dur)
            led.value(0)
            utime.sleep(dur)

while True:
    
    blink(0.5, mode)