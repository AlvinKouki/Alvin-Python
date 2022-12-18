from mcu_def import gpio
from time import sleep
from machine import Pin, ADC
from hcsr04 import HCSR04
import dht
import json

earthquake = Pin(gpio.SDD3, Pin.IN)

while 1:
    print(earthquake.value())
    if earthquake.value() == 1:
        print("emergency!")
    sleep(1)