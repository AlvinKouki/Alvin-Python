from machine import Pin, PWM
import time

f = 1000
d = 0
p2 = PWM(Pin(2), freq=f, duty=d)

while 1:
    for i in range(1024):
        p2.duty(i)
        time.sleep(0.001)

    for i in range(1024, -1, -1):
        p2.duty(i)
        time.sleep(0.001)
