import sys                                  # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging                              # Importuje moduł logging do obsługi logowania komunikatów
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")    # Ustawia poziom logowania na INFO i logowanie do pliku logfile.log
#logging.basicConfig(level=logging.DEBUG)    # Ustawia poziom logowania na DEBUG
print(f"""Podaj działanie które chcesz wykonać:
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie""")
operation = input("Wpisz numer działania (1/2/3/4): ")  # Pobiera od użytkownika numer działania
