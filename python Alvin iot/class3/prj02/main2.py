from machine import Pin
from time import sleep
from mcu_def import gpio

RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

while True:
    RED.value(1)
    sleep(1)
    RED.value(0)
    GREEN.value(1)
    sleep(1)
    GREEN.value(0)
    RED.value(1)
    GREEN.value(1)
    sleep(1)
    GREEN.value(0)
    RED.value(0)
