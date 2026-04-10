# To będzie główny plik wykonawczy całego projektu.
import os
from components.getMaxID import get_max_device_id
from components.device_generator import create_new_devices
from components.device import Device
from components.runSimulation import run_simulation

# # Odkomentuj dla Unix/Linux
# import subprocess
# project_directory = "ET_PROGRAMOWANIE"
# subprocess.run(["chmod", "-R", "755", project_directory])
# subprocess.run(["chown", "-R" "mateusz:mateusz", project_directory])
# # Koniec sekcji Unix/Linux
NumOfDevicesToCreate = 3
create_new_devices(NumOfDevicesToCreate, get_max_device_id(), "./devices")


# Ścieżka do folderu z urządzeniami
path = "./devices"

devices_list = []

# Sprawdzamy, czy katalog istnieje
if os.path.exists(path):
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            full_path = os.path.join(path, filename)
            
            new_device = Device.from_json(full_path)
            
            devices_list.append(new_device)

    print(f"Pomyślnie wczytano {len(devices_list)} urządzeń.")
else:
    print("Folder 'devices' nie istnieje!")

run_simulation(path)
