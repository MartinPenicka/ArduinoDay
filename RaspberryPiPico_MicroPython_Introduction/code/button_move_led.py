from machine import Pin
import utime

pins = [2,3,4,5,6,7,8,9]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))

for led in leds:
    led.value(1)

curr_led = 5
leds[curr_led].value(0)

last_click_time = 0
debounce_delay = 150
    
def move_led_left(pin):
    global mode, counter, last_click_time, debounce_delay, curr_led
    
    curr_time = utime.ticks_ms()
    time_diff = utime.ticks_diff(curr_time, last_click_time)
    last_click_time = curr_time
    
    if time_diff < debounce_delay:
        return
    
    leds[curr_led].value(1)
    curr_led += 1
    if curr_led == len(leds):
        curr_led = 0
            
    leds[curr_led].value(0)
    
def move_led_right(pin):
    global mode, counter, last_click_time, debounce_delay, curr_led
    
    curr_time = utime.ticks_ms()
    time_diff = utime.ticks_diff(curr_time, last_click_time)
    last_click_time = curr_time
    
    if time_diff < debounce_delay:
        return
    
    leds[curr_led].value(1)
    
    curr_led -= 1
    if curr_led < 0:
        curr_led = len(leds) - 1
        
    leds[curr_led].value(0)
    
    
button_left = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button_left.irq(trigger=machine.Pin.IRQ_FALLING, handler=move_led_left)

button_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button_right.irq(trigger=machine.Pin.IRQ_FALLING, handler=move_led_right)
    

while True:

    utime.sleep(10)