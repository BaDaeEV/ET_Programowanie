# To będzie główny plik wykonawczy całego projektu.
import os
import time
from components.getMaxID import get_max_device_id
from components.device_generator import create_new_devices
from components.runSimulation import run_simulation

# # Odkomentuj dla Unix/Linux
# import subprocess
# project_directory = "ET_PROGRAMOWANIE"
# subprocess.run(["chmod", "-R", "755", project_directory])
# subprocess.run(["chown", "-R" "mateusz:mateusz", project_directory])
# # Koniec sekcji Unix/Linux

# Default variables
DevicesPath = "./devices"
create_new_devices(10, get_max_device_id(), DevicesPath, True)
run_simulation(DevicesPath)




