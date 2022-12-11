from hcsr04 import HCSR04
from mcu_def import gpio
from time import sleep

sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)

while True:
    distance = sensor.distance_cm()
    print('Distance', distance, 'cm')
    sleep(1)
