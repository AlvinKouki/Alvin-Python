from umqtt.simple import MQTTClient
import time
from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
from mcu_def import gpio, mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

mq_server = "singularmakers.asuscomm.com"
mq_id = "singular"
mq_user = "singular"
mq_pass = "1234"
mqClient0 = MQTTClient(mq_id,
                       mq_server,
                       user=mq_user,
                       password=mq_pass,
                       keepalive=30)

try:
    mqClient0.connect()
except Exception as e:
    print(e)
    exit()
finally:
    print("connected MQTT server")


def on_message(topic, msg):
    msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"my subscribe topic:{topic}, msg:{msg}")
    lcd.clear()
    lcd.putstr(f"topic:{topic}")
    lcd.move_to(0, 1)
    lcd.putstr(f"msg:{msg}")


mqClient0.set_callback(on_message)
mqClient0.subscribe("Alvin")

while 1:
    mqClient0.check_msg()
    mqClient0.ping()
    time.sleep(1)
