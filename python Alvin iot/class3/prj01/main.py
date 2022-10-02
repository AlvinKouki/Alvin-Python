from machine import I2C, Pin
from time import sleep
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
p2 = Pin(2, Pin.OUT)

while 1:
    p2.value(0)
    lcd.putstr("nothing")
    sleep(1)
    lcd.clear()

    p2.value(1)
    lcd.putstr("fifrjfh")
    sleep(1)
    lcd.clear()
