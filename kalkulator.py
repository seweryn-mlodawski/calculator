import sys                                  # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging                              # Importuje moduł logging do obsługi logowania komunikatów
logging.basicConfig(level=logging.DEBUG)    # Ustawia poziom logowania na DEBUG
print(f"""Podaj działanie które chcesz wykonać:
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie""")
operation = input("Wpisz numer działania (1/2/3/4): ")  # Pobiera od użytkownika numer działania
