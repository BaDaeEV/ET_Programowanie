import os
import json
import shutil

#Importujemy biblioteki zewnętrzne niezbędne do działania programu.

#Tworzymy funkcję zmiennych 'count','start_index','path','ask'

def create_new_devices(count, start_index=0, path="../devices", ask=True): #definiujemy
    # path = "./devices" Zależnie od miejsca wykonania do modyfikacji ścieżka
    
    if ask:
        while True: 
            #Jeżeli 'ask' będzie prawdziwy, to w nieskończoność będzie się odtwarzać poniższa pętla 'while'
            #Poniższe 9 lini kodu to delikatna szata graficzna, tworzymy panel - 'menu urządzeń' i dajemy do wyboru 4 funkcje wyboru dotyczące urządzenia
            #choice = input().upper() Czyli czekamy na odpowiedź w terminalu i litera wciśniętego klawisza zostanie przypisana do zmiennej 'choice'.
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

            #Sprawdzana jest wartość zmiennej 'choice' w 'if' - Jeżeli będzie pasowała do któregokolwiek wspomnianego wcześniej wyboru to uaktywni się odpowiednia część kodu.
            if choice == "S":
                print("Pomijam tworzenie urządzeń.")
                return
            #W tym przypadku część kodu dotyczy S, czyli pominięcia i kontynuowania. Krótki komunikat i return który kończy funkcję.
            # 'elif' czyli jeżeli literą nie będzie S, a np. C to komenda shutil.rmtree usunue nam pliki od wybranej ścieżki - zmienna 'path'
            #Dodatkowo, mamy obsługę błędu gdyby usunięcie się nie powiodło to komunikat pod 'except' nas o tym poinformuje.
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
            #Jeżeli choice będzie równy "O", to wyświetlamy komunikat o nadpisywaniu danych z obsługą błędu i następnie zerujemy zmienną lokalną 'start_index' i za pomocą 'break' wychodzimy z funkcji.
            #Nadpisujemy dane usuwając istniejące i w ich miejscu wpisując te same zmienione o odpowiednie rekordy.
            elif choice == "A":
                print("Kontynuuję dodawanie...")
                # Dodawany index_start przez getMaxID.py
                break
            #Dla każdego innego wciśnięcia klawisza załącza nam się kod pod 'else'
            #Wyświetla nam komunikat o błędzie jakim jest wciśnięcie klawisza innego niż możliwe do wyboru.
            #else nie kończy nam funkcji, ta się zaczyna od nowa w pętli 'while'.
            else:
                print(f"Błąd: '{choice}' to nieprawidłowy wybór. Spróbuj ponownie.")

        if not os.path.exists(path):
            os.makedirs(path)
                #Sprawdzamy czy istnieje ścieżka, jeżeli takiej nie ma to ją tworzymy.
        for i in range(start_index, start_index + count):
            #Wyliczamy przy pomocy pętli 'for'. Liczymy to dla zakresu od start_index do start_index + count.
            device_ID = f"Device_{i}"
            #Dla każdego wyniku - urządzenia przypisujemy adres ID.
            jsonObj_conf = {
                "id": device_ID,
                "type": None,
                "power": None
            }
            #Konfigurujemy dane urządzenie jako obiekt json. Nie przypisujemy mu żadnego typu lub mocy - jedynie adres ID wcześniej nadany.
            
            with open(f"{path}/{device_ID}.json", "w") as file:
                json.dump(jsonObj_conf, file, indent=4)
                #Przy ścieżce otwartej jako plik .json "w" od "write" wrzucamy tam obiekt.

    print(f"Wygenerowano boilerplate dla {count} urządzeń (start od {start_index}).")