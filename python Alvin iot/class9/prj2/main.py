import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.username_pw_set("singular", "1234")
client.connect("singularmakers.asuscomm.com", 1883, 60)

while True:
    msg = input("please enter the message you want to upload on MQTT:")
    client.publish("Alvin", msg)
    time.sleep(0.3)