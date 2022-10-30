from http import client
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print('Connected with result code' + str(rc))
    client.subscribe("GOD COOKIE Alvin")


#小鈴鐺功能
def on_message(client, userdata, msg):
    print(
        f"the topic I subscribe is:{msg.topic}, receive message:{msg.payload.decode('utf-8')}"
    )


client = mqtt.Client()
client.on_connect = on_connect  #設定連線
client.on_message = on_message  #設定接受訊息
client.username_pw_set("singular", "1234")  #設定登入帳號密碼

client.connect("singularmakers.asuscomm.com", 1883, 60)
client.loop_forever()