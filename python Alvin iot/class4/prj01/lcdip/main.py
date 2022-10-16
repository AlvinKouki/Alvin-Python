import network
from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd

wlSSID = "SingularClass0"
wlPWD = "Singular#1234"
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wlan.scan()
wlan.connect(wlSSID, wlPWD)

while not (wlan.isconnected()):
    pass
print("connect successfully", wlan.ifconfig())

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.putstr(wlan.ifconfig()[0])
lcd.move_to(0, 1)
lcd.putstr("It's working!")