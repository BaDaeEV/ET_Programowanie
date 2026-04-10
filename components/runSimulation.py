import time
import os
from components.device import Device

def run_simulation(devices_path):
    active_Devices = []

    if os.path.exists(devices_path):
        for file_name in os.listdir(devices_path):
            if file_name.endswith(".json"):
                full_path = os.path.join(devices_path, file_name)
                # Tworzenie instancji klasy urządzenia
                d = Device.from_json(full_path)
                # Uruchamianie wątku dla instancji klasy // Urządzenia
                d.start()
                active_Devices.append(d)
    print(f"Uruchomiono łącznie {len(active_Devices)} generatorów.")

    # Runtime loop
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\nZamykanie Symulacji...")
        for d in active_Devices:
            d.stop()
