# To będzie główny plik wykonawczy całego projektu.
import os
from components.getMaxID import get_max_device_id
from components.device_generator import create_new_devices

# # Odkomentuj dla Unix/Linux
# import subprocess
# project_directory = "ET_PROGRAMOWANIE"
# subprocess.run(["chmod", "-R", "755", project_directory])
# subprocess.run(["chown", "-R" "mateusz:mateusz", project_directory])
# # Koniec sekcji Unix/Linux

create_new_devices(10, get_max_device_id(), "./devices")