from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
from mcu_def import gpio, mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.putstr(wlan.ip)
lcd.move_to(0, 1)
lcd.putstr("It's working!")