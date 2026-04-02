import paho.mqtt.client as mqtt
import time

# 1. Ustawienia
BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/device_01/power"

# 2. Inicjalizacja klienta (Ważne: VERSION2 dla nowych bibliotek)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 3. Połączenie
try:
    client.connect(BROKER, PORT, 60)
    
    # Rozpoczęcie pętli obsługującej komunikację w tle
    client.loop_start()

    # 4. Odbieranie
        def on_message(client, userdata, msg)

    # Krótka pauza, żeby upewnić się, że wiadomość "wyleciała" z bufora
    time.sleep(1)
    
    client.loop_stop()
    client.disconnect()

except Exception as e:
    print(f"Nie udało się połączyć: {e}")