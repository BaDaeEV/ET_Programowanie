# ET_Programowanie
Projekt dot IoT w połączeniu z aktywnym zarządzaniem urządzeniami, które dla oszczędzania enegii chcemy  przełączać w tryb standby.

# Info dla pythona, żeby tą ścieżkę traktować jako __init__
localPath="/home/mateusz/Pulpit/Praca + studia/ET_Programowanie"
export PYTHONPATH=$PYTHONPATH:$($localPath)
source .venv/bin/activate


device_ID - Numer identyfikacyjny urządzenia [string]
type - Typ urządzenia [string]
power - Pobierana moc w [W] [float]
state - Status urządzenia - [Włączone / Wyłączone] [Bolean]
standBy - Tryb oszczędzania energii [Boolean]