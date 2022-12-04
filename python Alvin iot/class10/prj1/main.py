from machine import Pin
from mcu_def import gpio, mcu_fun
import dht
import time
import json

d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu = mcu_fun()
mcu.connect_ap('SingularClass0', 'Singular#1234')
mcu.mqtt_subscribe(mq_id="Alvin")
lcd = mcu.lcd_initial(sda_pin=4, scl_pin=5)
msg_json = {}

while 1:
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"Humidity:{hum:02d}, Temperature: {temp:02d}{'\u00b0'}C")
    mcu.mqtt_put_msg(
        topic="Alvin",
        msg=f"Humidity:{hum:02d}, Temperature: {temp:02d}{'\u00b0'}C")
    lcd.clear()
    lcd.putstr(f"Humidity:{hum:02d}")
    lcd.move_to(0, 1)
    lcd.putstr(f"Temperature: {temp:02d}{'\u00b0'}C")
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    mcu.mqtt_put_msg(topic='Alvin', msg=json.dumps(msg_json))
    time.sleep(1)
