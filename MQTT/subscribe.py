import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    topic = msg.topic              # np. pusage/device_01
    payload = msg.payload.decode()  # np. "30"

    device_id = topic.split("/")[1]

    print(f"Urządzenie: {device_id}, moc: {payload} W")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("pusage/#")

client.loop_forever()