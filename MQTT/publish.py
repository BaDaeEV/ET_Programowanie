import paho.mqtt.client as mqtt
import time
from components.logger import writeToLog

# 1. Ustawienia
BROKER = "localhost"
PORT = 1883
UID = "Device_01"
TOPIC = "pusage/{}".format(UID)

# 2. Inicjalizacja klienta (Ważne: VERSION2 dla nowych bibliotek)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


    # 3. Połączenie
def publishToTopic(topic, data):
    try:
        client.connect(BROKER, PORT, 60)
        
        # Rozpoczęcie pętli obsługującej komunikację w tle
        client.loop_start()

        # 4. Publikowanie
        result = client.publish(topic, data)
        
        # Sprawdzenie czy wysłano
        status = result.rc
        if status == 0:
            writeToLog(topic, data, status)
        elif status == 1:
            writeToLog(topic, data, status)
        else:
            writeToLog(topic, data, status)
        
        client.loop_stop()
        client.disconnect()

    except Exception as e:
        print(f"Nie udało się połączyć: {e}")

publishToTopic(TOPIC, "8W")
publishToTopic(TOPIC, "14W")
publishToTopic(TOPIC, "310W")