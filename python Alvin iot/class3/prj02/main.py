from machine import Pin, PWM
from time import sleep
from mcu_def import gpio

f = 1000
d = 0
RED = PWM(Pin(gpio.D5), freq=f, duty=d)
GREEN = PWM(Pin(gpio.D6), freq=f, duty=d)
BLUE = PWM(Pin(gpio.D7), freq=f, duty=d)

while True:
    for duty_cycle in range(1023, -1, -1):
        RED.duty(duty_cycle)
        GREEN.duty(1023 - duty_cycle)
        sleep(0.001)
    for duty_cycle in range(1023, -1, -1):
        GREEN.duty(duty_cycle)
        BLUE.duty(1023 - duty_cycle)
        sleep(0.001)
    for duty_cycle in range(1023, -1, -1):
        BLUE.duty(duty_cycle)
        RED.duty(1023 - duty_cycle)
        sleep(0.001)
