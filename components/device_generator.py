import os
import json
import shutil

def create_new_devices(count, start_index=0, path="../devices", ask=True):
    # path = "./devices" Zależnie od miejsca wykonania do modyfikacji ścieżka
    
    if ask:
        while True: 
            print("\n" + "="*30)
            print(f"{'MENU URZĄDZEŃ':^30}")
            print("="*30)
            # Używamy wyrównania f-string, aby opisy były w jednej linii
            print(f"{'A - Add':<15} (Dodaj nowe)")
            print(f"{'S - Skip':<15} (Pomiń i kontynuuj)")
            print(f"{'O - Overwrite':<15} (Wyczyść i stwórz nowe)")
            print(f"{'C - Clear':<15} (Tylko usuń pliki)")
            choice = input().upper()
            print("=" * 30)

            if choice == "S":
                print("Pomijam tworzenie urządzeń.")
                return
            
            elif choice == "C":
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    print(f"BŁĄD podczas usuwania: {e}")
                return
            
            elif choice == "O":
                print("Nadpisuję istniejące dane...")
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    print(f"BŁĄD podczas usuwania: {e}")
                start_index = 0
                break
            
            elif choice == "A":
                print("Kontynuuję dodawanie...")
                # Dodawany index_start przez getMaxID.py
                break
            
            else:
                print(f"Błąd: '{choice}' to nieprawidłowy wybór. Spróbuj ponownie.")

        if not os.path.exists(path):
            os.makedirs(path)
                
        for i in range(start_index, start_index + count):
            device_ID = f"Device_{i}"
            jsonObj_conf = {
                "id": device_ID,
                "type": None,
                "power": None
            }
            
            with open(f"{path}/{device_ID}.json", "w") as file:
                json.dump(jsonObj_conf, file, indent=4)

    print(f"Wygenerowano boilerplate dla {count} urządzeń (start od {start_index}).")