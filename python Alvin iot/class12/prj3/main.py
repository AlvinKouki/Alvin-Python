from machine import Pin, ADC, PWM
from mcu_def import gpio, mcu_fun
from hcsr04 import HCSR04
import dht
import time
import json

mcu = mcu_fun()
RED, GREEN, BLUE = mcu.led_initial(r_pin=gpio.D5,
                                   b_pin=gpio.D6,
                                   g_pin=gpio.D6,
                                   pwm=True)
sg_pin = PWM(Pin(gpio.D8), freq=50, duty=0)
mcu.servo_angle(sg_pin, 180)
time.sleep(1)
sensor = HCSR04(trigger_pin=gpio.SDD2, echo_pin=gpio.SDD2)


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    lcd.clear()
    lcd.putstr(f"topic:{topic}")
    lcd.move_to(0, 1)
    lcd.putstr(f"msg:{msg}")
    if msg == "on":
        RED.duty(1023)
        GREEN.duty(1023)
        BLUE.duty(1023)
    elif msg == "off":
        RED.duty(0)
        GREEN.duty(0)
        BLUE.duty(0)


d = dht.DHT11(Pin(gpio.D0, Pin.IN))
mcu.connect_ap('SingularClass0', 'Singular#1234')
mcu.mqtt_subscribe(mq_id="Alvin", callback=on_message)
lcd = mcu.lcd_initial(sda_pin=4, scl_pin=5)
msg_json = {}
adc = ADC(0)

while 1:
    distance = sensor.distance_cm()
    value = adc.read()
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    lcd.clear()
    lcd.putstr(f"Humidity:{hum:02d}")
    lcd.move_to(0, 1)
    lcd.putstr(f"Temperature: {temp:02d}{'\u00b0'}C")

    if distance < 10:
        mcu.servo_angle(sg_pin, 90)
        msg_json["gate"] = True
        mcu.mqtt_put_msg(topic='Alvin', msg=json.dumps(msg_json))
        time.sleep(3)
        mcu.servo_angle(sg_pin, 180)
        msg_json["gate"] = False
    else:
        mcu.servo_angle(sg_pin, 180)
        msg_json["gate"] = False

    msg_json["distance"] = distance
    msg_json["humidity"] = hum
    msg_json["temperature"] = temp
    msg_json["lightsensor"] = value

    mcu.mqtt_put_msg(topic='Alvin', msg=json.dumps(msg_json))
    mcu.mqtt_get_msg(topic='Alvin')
    time.sleep(1)
