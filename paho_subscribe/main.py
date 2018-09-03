import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/api/cluster")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#client = mqtt.Client("control1",transport='websockets')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("43.251.98.16",1883,60)
#client.connect("209.97.168.161", 1883, 60)
#client.connect("209.97.168.161", 8083, 60)
client.loop_forever()

