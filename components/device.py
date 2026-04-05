import json
import random

class Device:
    def __init__(self, device_ID, model="Standard", power=0):
        self.deviceID = device_ID
        self.model = model
        self.power = power

    @classmethod
    def from_json(cls, file_path):
        # Tworzenie obiektu z pliku .json
        with open(file_path, 'r') as file:
            data = json.load(file)
        return cls(data['id'], data['model'], data['power'])
    
    def generate_power(self):
        # Symulacja zmiennego poboru energii elektrycznej
        variation = random.uniform(-3, 3)
        self.power = max(0, self.power + variation)
        return round(self.power, 2)


