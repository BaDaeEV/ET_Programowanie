import paho.mqtt.client as mqtt
import threading
import random
import yaml
import time
import os
import matplotlib.pyplot as plt

### ============== Config ========== ###
HOST = "127.0.0.1"
PORT = 10650
KEEPALIVE = 60
### ========= Devices config ======= ###
with open("./configuration/devicesTypes.yaml", "r") as file:
    Yconfig = yaml.safe_load(file)
    available_types = list(Yconfig["types"].keys())

### ================================ ###

class Device:
    def __init__(self, deviceID, deviceType=None, statesConfig=None):
        self.deviceID = deviceID
        self.deviceType = deviceType
        self.statesConfig = Yconfig["types"][self.deviceType]["states"] # OFF z racji default state == OFF
        # Parametry mocy
        self.currentPower = 0.0
        
        # Logika stanów
        self.state = "OFF" # OFF, ON, STANDBY
        self.running = False # True/False - status uruchomienia procesu generowania pomiarów w wątku.

        #Domyślne dla każdego urządzenia
        self._client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=self.deviceID)
        self._thread = None
        self._history = []
    
    def set_state(self, new_state):
        #Metoda do zmiany stanu urządzenia
        if new_state in ["OFF", "ON", "STANDBY"]:
            self.state = new_state
            self.statesConfig = Yconfig["types"][self.deviceType]["states"]
            print(f"[{self.deviceID}] Zmiana stanu na: {new_state}")
    
    def change_state(self):
        activationPoint = 1.85
        activationValue = 0
        for i in range(0,2):
            activationValue += random.random()
        if activationValue >= activationPoint:
            self.running = False
            self._thread.

    def generateData(self):
        # Parametry bezwładności (im mniejszy step, tym wolniejsza zmiana)
        ADJUSTMENT_STEP = 0.15
        try:
            while self.running == True:
                currentStateCfg = self.statesConfig[self.state]
                basePower = currentStateCfg["base"]
                peakPower = currentStateCfg["peak"]
                # Sprawdzanie średniej mocy pobiarnej z ostatniej minuty
                avg = lambda aPwr: sum(aPwr) / len(aPwr) if aPwr else 0
                avgMinutePower = avg(self._history)
                if avgMinutePower >= peakPower * 0.8:
                    self.set_state("OFF")
                # --- #
                self.monitorHistory()

                if self.state == "OFF":
                    # Równie dobrze można ustawić na sztywno 0.0, ale zakładam że OFF może nie zawsze nic nie pobierać
                    target_power = basePower 
                elif self.state == "STANDBY":
                    target_power = basePower + random.uniform(-0.05, 0.05) # Generowanie lekkiego szumu w standby
                elif self.state == "ON" and self.currentPower > peakPower * 0.95:
                    self.currentPower -= (peakPower * 0.1) # Nagły spadek
                else:
                    target_power = random.uniform(basePower, peakPower)
                    if target_power >= peakPower:
                        target_power = peakPower
                
                    diff = target_power - self.currentPower
                    self.currentPower += diff * ADJUSTMENT_STEP # Założenie płynnego przejścia
                    self.currentPower = round(self.currentPower, 2)

                # Odstęp między generowanymi wartościami w Sekundach
                time.sleep(1)

        except Exception as e:
            print(f"Uruchomienie generowania poboru mocy dla {self.deviceID} o nazwie {self.deviceType} \
                    zakończyło się błędem: {e}")
    def monitorHistory(self):
        try:
            self._history.append(self.currentPower)
            if len(self._history) > 60:
                self._history.pop(0)
        except Exception as e:
            print(f"Wystąpił błąd {e}")
    

    def start(self):
        try:
            self._client.connect(host=HOST, port=PORT, keepalive=KEEPALIVE)
            self._client.loop_start()

            #Uruchomienie urządzenia w wątku, aby nie blokować potoku głównego terminala
            if self._thread is None or not self._thread.is_alive():
                self.running = True
                self._thread = threading.Thread(target=self.generateData, daemon=True)
                self._thread.start()
                

        except Exception as e:
            print(f"Nie udało się połączyć, '{e}'")

    def show_diagram(self):
        """Wyświetla okno z wykresem ostatnich 80 wyników"""
        if not historia_pomiarow:
            print("Brak danych do wyświetlenia wykresu.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(historia_pomiarow, color='tab:blue', linewidth=2, label='Pobór [W]')
        
        # Estetyka wykresu
        plt.title(f"Pobór mocy w czasie: {self.deviceID} ({self.deviceType})")
        plt.xlabel("Ostatnie próbki")
        plt.ylabel("Moc [W]")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        
        # Wyświetlenie okna
        plt.show()

    def stop(self):
        #Zatrzymywanie generowania poboru energii elektrycznej w tle
        self.running = False
# rvc = random.choice(available_types)
# d = Device(0, rvc, Yconfig["types"][rvc]["states"]["OFF"])

# getattr(d)
# print(Yconfig["types"][random.choice(available_types)]["states"]["ON"])
# print(random.choice(available_types))

# 1. Losujemy typ
rvc = random.choice(available_types)

# 2. Inicjalizujemy obiekt
d = Device(deviceID="Dev_01", deviceType=rvc)
d.start()
d.set_state("ON")
historia_pomiarow = []
for i in range(0,100):
    # 3. Wyświetlamy stan obiektu "na sztywno"
    print("--- Stan obiektu po inicjalizacji ---")
    for klucz, wartosc in d.__dict__.items():
        # Pomijamy wyświetlanie całego obiektu klienta MQTT, żeby nie zaśmiecać konsoli
        if klucz == "_client":
            print(f"{klucz}: <MqttClient Object>")
            continue
        print(f"{klucz}: {wartosc}")
    print("-------------------------------------")
    historia_pomiarow.append(d.currentPower)
    time.sleep(1)
    if i == 400:
        d.set_state("STANDBY")
    if i == 750:
        d.set_state("ON")
    
    os.system("clear")
print(historia_pomiarow)
d.show_diagram()
time.sleep(10)