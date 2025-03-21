from machine import Pin
import utime

sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / 65535

while True:
    
    reading = sensor_temp.read_u16()
    voltage = reading * conversion_factor
    temperature = 27 - (voltage - 0.706) / 0.001721
    print("Temperature:", temperature, "°C")
    utime.sleep(1)