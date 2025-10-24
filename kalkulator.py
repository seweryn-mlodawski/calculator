import sys                                  # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging                              # Importuje moduł logging do obsługi logowania komunikatów
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")    # Ustawia poziom logowania na INFO i logowanie do pliku logfile.log
#logging.basicConfig(level=logging.DEBUG)    # Ustawia poziom logowania na DEBUG

# Definiuje słownik działań z nazwami, funkcjami i komunikatami
dzialania = {
    '1': ('Dodawanie', lambda x, y: x + y, "Dodaję"), 
    '2': ('Odejmowanie', lambda x, y: x - y, "Odejmuję"),
    '3': ('Mnożenie', lambda x, y: x * y, "Mnożę"),
    '4': ('Dzielenie', lambda x, y: x / y, "Dzielę")
}

print(f"""Jakie działanie chcesz wykonać:
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie""")

while True:
    print("Podaj numer działania (1/2/3/4): ", end="") 
    typ = input() # Pobiera od użytkownika wybór działania
    if typ in dzialania:
        break
    else:
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
    logging.error("Podano nieprawidłowe działanie: %s" % typ) # Loguje błąd nieprawidłowego działania
       
print("Podaj liczbę 1.", end=" ") 
a = float(input()) # Pobiera pierwszy składnik od użytkownika
print("Podaj liczbę 2.", end=" ")
b = float(input()) # Pobiera drugi składnik od użytkownika

nazwa, operacja, log_msg = dzialania[typ] # Pobiera nazwę, funkcję i komunikat logowania dla wybranego działania
logging.info(f'{log_msg} {a:.2f} i {b:.2f}') # Loguje informację o wykonywanym działaniu
print(f"{log_msg} {a:.2f} i {b:.2f}") # Drukuje komunikat o wykonywanym działaniu

wynik = operacja(a, b) # Wykonuje wybrane działanie
print(f"Wynik to {wynik:.2f}") # Drukuje wynik działania
logging.info("Wynik to %.2f" % wynik) # Loguje wynik działania