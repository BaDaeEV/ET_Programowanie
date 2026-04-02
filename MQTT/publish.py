import paho.mqtt.client as mqtt
import time

# 1. Ustawienia
BROKER = "localhost"
PORT = 1883
TOPIC = "sensors/device_01/power"
PAYLOAD = "250.5" # Twoja symulowana moc w Watach

# 2. Inicjalizacja klienta (Ważne: VERSION2 dla nowych bibliotek)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 3. Połączenie
try:
    client.connect(BROKER, PORT, 60)
    
    # Rozpoczęcie pętli obsługującej komunikację w tle
    client.loop_start()

    # 4. Publikowanie
    result = client.publish(TOPIC, PAYLOAD)
    
    # Sprawdzenie czy wysłano
    status = result.rc
    if status == 0:
        print(f"Wysłano '{PAYLOAD}' do tematu: {TOPIC}")
    else:
        print(f"Błąd wysyłania do tematu {TOPIC}")

    # Krótka pauza, żeby upewnić się, że wiadomość "wyleciała" z bufora
    time.sleep(1)
    
    client.loop_stop()
    client.disconnect()

except Exception as e:
    print(f"Nie udało się połączyć: {e}")