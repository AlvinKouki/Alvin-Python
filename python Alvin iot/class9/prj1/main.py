import time
from mcu_def import gpio, mcu_fun

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")
RED, GREEN, BLUE = wlan.led_initial(r_pin=gpio.D5,
                                    b_pin=gpio.D6,
                                    g_pin=gpio.D6,
                                    mode='pwm')

lcd = wlan.lcd_initial(sda_pin=4, scl_pin=5)


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


wlan.mqtt_subscribe(mq_id='Alvin', callback=on_message)

while 1:
    wlan.mqtt_get_msg(topic='Alvin')
    time.sleep(0.3)
