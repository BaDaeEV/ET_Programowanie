import json
import random
import time
import threading
import paho.mqtt.client as mqtt
from components.logger import writeToLog
PORT = 13644
BROKER = "localhost"
class Device:
    def __init__(self, device_ID, type="Standard", power=0, state=True, standBy=False):
        self.deviceID = device_ID
        self.type = type
        self.power = power if power is not None else 0
        self.state = state
        self.standBy = standBy
        self._thread = None
        
        #Tworzenie klienta dla serwera MQTT
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.deviceID)
    @classmethod
    def from_json(cls, file_path):
        # Tworzenie obiektu z pliku .json
        with open(file_path, 'r') as file:
            data = json.load(file)
        return cls(data['id'], data['type'], data['power'])

    def _run_generation(self):
        # Metoda używana do uruchomienia generowania "pomiarów" poboru mocy
        # W osobnych wątkach celem niezależnego uruchamiania wielu urządzeń
        try:
            # Rozpoczęcie komunikacji z serwerem MQTT
            self.client.connect(BROKER, PORT, 60)
            self.client.loop_start()
            # Rzeczywiste ciało funkcji

            while self.state:
                variation = random.uniform(-3, 3)
                self.power = max(0, self.power + variation)
                TOPIC = "pusage/{}".format(self.deviceID)
                PAYLOAD = round(self.power, 2)

                # KLUCZ: Używamy metody self.client, a nie zewnętrznej funkcji!
                result = self.client.publish(TOPIC, PAYLOAD)

                # Logowanie wysłanych danych (debug)
                status = result.rc
                if status == 0:
                    writeToLog(TOPIC, PAYLOAD, status)
                elif status == 1:
                    writeToLog(TOPIC, PAYLOAD, status)
                else:
                    writeToLog(TOPIC, PAYLOAD, status)
                
                # Czas pomiędzy pomiarami
                time.sleep(1)
            # Zakończenie komunikacji z serwerem MQTT    
            self.client.loop_stop()
            self.client.disconnect()

        except Exception as e:
            print(f"Nie udało się połączyć: {e}")
    
    def start(self):
        try:
            self.client.connect("localhost", 13644, 60)
            self.client.loop_start() 
        except Exception as e:
            print(f"Błąd połączenia dla {self.deviceID}: {e}")
            return

        # 2. Uruchamia Twój wątek generujący liczby
        if self._thread is None or not self._thread.is_alive():
            self.state = True
            self._thread = threading.Thread(target=self._run_generation, daemon=True)
            self._thread.start()
    
    def stop(self):
        # Zatrzymuje generowanie mocy w tle
        self.state = False






