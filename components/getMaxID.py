import os
# Wyszukiwanie największego ID w obecnie stworzonych urządzeniach
def get_max_device_id(directory="./devices"):
    if not os.path.exists(directory):
        return 0
    
    ids = []
    for filename in os.listdir(directory):
        if filename.startswith("Device_") and filename.endswith(".json"):
            try:
                number = int(filename.split('_')[1].split('.')[0])
                ids.append(number)
            except (IndexError, ValueError):
                continue
    
    return max(ids) if ids else 0