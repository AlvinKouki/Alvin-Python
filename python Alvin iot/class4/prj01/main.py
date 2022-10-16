from time import sleep, time
from machine import Pin, ADC, PWM
from mcu_def import gpio

adc = ADC(0)

f = 1000
d = 0
RED = PWM(Pin(gpio.D5), freq=f, duty=d)
GREEN = PWM(Pin(gpio.D6), freq=f, duty=d)
BLUE = PWM(Pin(gpio.D7), freq=f, duty=d)

while 1:
    value = adc.read()
    print(f'value={value}, {round(value*100/1024)}%')

    if (int(value) > 650):

        RED.duty(value)
        BLUE.duty(value)
        GREEN.duty(value)

    else:
        RED.duty(0)
        BLUE.duty(0)
        GREEN.duty(0)
