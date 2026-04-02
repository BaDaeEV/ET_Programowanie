import datetime
import random
class Device:
    def __init__(self, device_id):
        self.id = device_id
        self.power_history = []
        self.state = "unknown"
        self.type = "unknown"

    def add_measurement(self, power, timestamp, *additionals):
        self.power_history.append((timestamp, power))
        if len(self.power_history) > 1000:
            self.power_history.pop(0)

    def get_features(self):
        powers = [p for _, p in self.power_history]
    
        if not powers:
            return None

        return {
            "mean": sum(powers) / len(powers),
            "min": min(powers),
            "max": max(powers),
            "std": (sum((p - sum(powers)/len(powers))**2 for p in powers) / len(powers))**0.5,
            "activity_ratio": sum(1 for p in powers if p > 5) / len(powers)
        }
    def get_type(self):
        return self.type
    
    def set_type(self, type):
         self.type = type


    
# dv = Device(1)
# currentDate = datetime.datetime.now()
# for i in range(100):
#     dv.add_measurement(random.randint(4,20), currentDate)
    
# print(dv.get_features())
# print(dv.power_history)
# dv.set_type("Charger")
# print(dv.id)

# print(dv.get_type())