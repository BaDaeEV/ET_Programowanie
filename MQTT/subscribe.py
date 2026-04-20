import paho.mqtt.client as mqtt
import time
import os
import threading
port = 13644
device_data = {}
def on_message(client, userdata, msg):
    topic = msg.topic              # np. pusage/device_01
    payload = msg.payload.decode()  # np. "30"

    device_id = topic.split("/")[1]

    if device_id not in device_data:
        device_data[device_id] = []
    
    device_data[device_id].append(payload)

def display_dashboard():
    """Funkcja działająca w osobnym wątku, odświeżająca widok."""
    while True:
        # Czyścimy konsolę (cls dla Windows, clear dla Linux/Mac)
        os.system('cls')
        
        print("=== MONITOR URZĄDZEŃ MQTT ===")
        print(f"Aktywnych urządzeń: {len(device_data)}")
        print("-" * 40)
        
        # Sortujemy po ID, żeby lista nie skakała
        for d_id in sorted(device_data.keys()):
            print(f"ID: {d_id:15} | Moc: {device_data[d_id]} W\n")
            
        print("-" * 40)
        print("Naciśnij Ctrl+C, aby zakończyć...")
        
        time.sleep(1) # Odświeżaj widok co sekundę

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
threading.Thread(target=display_dashboard, daemon=True).start()

client.connect("localhost", port, 60)
client.subscribe("pusage/#")
client.loop_forever()

