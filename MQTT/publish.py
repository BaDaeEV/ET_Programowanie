import paho.mqtt.client as mqtt
import time
from components.logger import writeToLog

# 1. Ustawienia
BROKER = "localhost"
PORT = 13644
UID = "Device_01"
TOPIC = "pusage/{}".format(UID)

# 2. Inicjalizacja klienta (VERSION2)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


# 3. Publikowanie
def publishToTopic(topic, data):
        result = client.publish(topic, data)
    
        # Sprawdzenie czy wysłano
        status = result.rc
        if status == 0:
            writeToLog(topic, data, status)
        elif status == 1:
            writeToLog(topic, data, status)
        else:
            writeToLog(topic, data, status)