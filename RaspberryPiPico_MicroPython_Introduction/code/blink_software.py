from machine import Pin
import utime

pins = [2,3,4,5,6,7,8,9]
leds = []

for pin in pins:
    leds.append(Pin(pin, Pin.OUT))

for led in leds:
    led.value(1)

curr_mode = -1
keep_blinking = False

last_click_time = 0
debounce_delay = 150

def leds_down():
    for led in leds:
        led.value(1)

def blink_all(dur):
    
    for led in leds:
        led.value(0)
        
    utime.sleep(dur)
    
    for led in leds:
        led.value(1)
        
    utime.sleep(1)
    
def blink_single_moving(dur):
    
    for led in leds:
        led.value(0)
        utime.sleep(dur)
        led.value(1)
        utime.sleep(dur)
        
def blink_fill_up(dur):
    
    for led in leds:
        led.value(0)
        utime.sleep(dur)
        
    for led in leds:
        led.value(1)
        
blink_methods = [blink_all, blink_single_moving, blink_fill_up]
    
def select_mode(pin):
    global mode, counter, last_click_time, debounce_delay, curr_mode
    
    curr_time = utime.ticks_ms()
    time_diff = utime.ticks_diff(curr_time, last_click_time)
    last_click_time = curr_time
    
    if time_diff < debounce_delay:
        return
    
    leds[curr_mode].value(1)
    curr_mode += 1
    if curr_mode == len(blink_methods):
        curr_mode = 0
        
    print(f"Selected method {curr_mode}")
            
    leds[curr_mode].value(0)
    
def start_stop_blinking(pin):
    
    global keep_blinking, curr_mode

    if not keep_blinking:
        print(f"Starting mode {curr_mode}")
        leds_down()
        
        keep_blinking = True
        
    else:
        print("Stopping")
        keep_blinking = False
        leds_down()
        leds[curr_mode].value(0)
    
button_left = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
button_left.irq(trigger=machine.Pin.IRQ_FALLING, handler=select_mode)

button_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button_right.irq(trigger=machine.Pin.IRQ_FALLING, handler=start_stop_blinking)
    
duration = 0.5

while True:

    if keep_blinking:
        blink_methods[curr_mode](duration)
        
    utime.sleep(0.5)