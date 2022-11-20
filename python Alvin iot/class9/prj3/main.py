from mcu_def import mcu_fun
from machine import ADC
import time

adc = ADC(0)
mcu = mcu_fun()
mcu.connect_ap('SingularClass0', 'Singular#1234')
mcu.mqtt_subscribe(mq_id="Alvin")

while True:
    value = adc.read()
    print(value)
    mcu.mqtt_put_msg(topic="Alvin", msg=str(value))
    time.sleep(0.3)
