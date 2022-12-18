from machine import UART, Pin
from mcu_def import gpio
from time import sleep

uart = UART(1, baudrate=9600)
uart.init(9600, bits=8, parity=None, stop=1)
earthquake = Pin(gpio.SDD3, Pin.IN)
buf1 = bytearray(5)
buf1[0] = 0xAA
buf1[1] = 0x13
buf1[2] = 0x01
buf1[3] = 0x7f
buf1[4] = buf1[0] + buf1[1] + buf1[2] + buf1[3]
uart.write(buf1)

while 1:
    print(earthquake.value())
    if earthquake.value() == 1:
        buf = bytearray(6)
        buf[0] = 0xAA
        buf[1] = 0x07
        buf[2] = 0x02
        buf[3] = 0x00
        buf[4] = 0x01
        buf[5] = buf[0] + buf[1] + buf[2] + buf[3] + buf[4]
        uart.write(buf)
        sleep(3)
    else:
        buf2 = bytearray(5)
        buf2[0] = 0xAA
        buf2[1] = 0x04
        buf2[2] = 0x00
        buf2[3] = 0xAE
        uart.write(buf2)
    sleep(1)