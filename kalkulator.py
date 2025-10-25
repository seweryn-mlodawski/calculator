import sys                                  # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging                              # Importuje moduł logging do obsługi logowania komunikatów
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")    # Ustawia poziom logowania na INFO i logowanie do pliku logfile.log
#logging.basicConfig(level=logging.DEBUG)    # Ustawia poziom logowania na DEBUG

# Definiuje słownik działań z nazwami, funkcjami i komunikatami
dzialania = {
    '1': ('Dodawanie (+)', lambda x, y: x + y, "Suma"),
    '2': ('Odejmowanie (-)', lambda x, y: x - y, "Różnica"), 
    '3': ('Mnożenie (*)', lambda x, y: x * y, "Iloczyn"),
    '4': ('Dzielenie (/)', lambda x, y: x / y, "Iloraz"),
}

print(f"""Jakie działanie chcesz wykonać:
1 - Dodawanie (+)
2 - Odejmowanie (-)
3 - Mnożenie (*)
4 - Dzielenie (/)
""")

while True:
    print("Podaj numer działania (1/2/3/4): ", end="") #end ="" zapobiega przejściu do nowej linii po wydrukowaniu
    typ = input() # Pobiera od użytkownika wybór działania
    if typ in dzialania:
        print("Wybrano:", dzialania[typ][0]) # Drukuje nazwę wybranego działania
        break
    else:
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
    logging.error("Podano nieprawidłowe działanie: %s" % typ) # Loguje błąd nieprawidłowego działania
       
while True:
    a = input("Podaj pierwszą liczbę: ") # Pobiera od użytkownika pierwszą liczbę
    b = input("Podaj drugą liczbę: ") # Pobiera od użytkownika drugą liczbę
    if a.isdigit() and b.isdigit(): # Sprawdza, czy obie wartości są liczbami - pierwszy punkt "Dla chętnych"
        a = float(a) # Konwertuje pierwszą liczbę na float
        b = float(b) # Konwertuje drugą liczbę na float   
        if typ == '4' and b == 0:
            print("Nie można dzielić przez zero, podaj drugą liczbę różną od 0.")
            logging.error("Próba dzielenia przez zero.") # Loguje błąd próby dzielenia przez zero
            continue
        break    
    else:
        print("Nieprawidłowe dane, możesz wpisać tylko liczby całkowite! Spróbuj ponownie.")
        logging.error("Wpisano nieprawidłowe znaki: %s, %s" % (a, b)) # Loguje błąd nieprawidłowych liczb   

nazwa, operacja, log_msg = dzialania[typ] # Pobiera nazwę, funkcję i komunikat logowania dla wybranego działania
logging.info(f'{log_msg} {a:.2f} i {b:.2f}') # Loguje informację o wykonywanym działaniu
print(f"{log_msg} {a:.0f} i {b:.0f}") # Drukuje komunikat o wykonywanym działaniu

wynik = operacja(a, b) # Wykonuje wybrane działanie
if wynik.is_integer():   # Sprawdza, czy wynik jest liczbą całkowitą
    #wynik jest liczba całkowitą
    print(f"Wynik to {int(wynik)}") # Drukuje wynik jako liczbę całkowitą
    logging.info("Wynik to %d" % int(wynik)) # Loguje wynik jako liczbę całkowitą
else:
    #wynik jest liczbą ułamkową
    print(f"Wynik to {wynik:.2f}") # Drukuje wynik jako liczbę zmiennoprzecinkową z dwoma miejscami po przecinku
    logging.info("Wynik to %.2f" % wynik) # Loguje wynik jako liczbę z dwoma miejscami po przecinku

# Koniec programu

def kalkulator_help():
    """
    Kalkulator wykonujący podstawowe działania matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie.
    Program prosi użytkownika o wybór działania oraz dwie liczby, a następnie wykonuje wybrane działanie i wyświetla wynik.
    Program obsługuje błędy, takie jak nieprawidłowy wybór działania, nieprawidłowe dane wejściowe oraz dzielenie przez zero.
    Wszystkie ważne zdarzenia są logowane do pliku logfile.log.
    Nie radzi sobie z liczbami ujemnymi podawanymi do obliczeń. do poprawy.
    
    Dodać pkt 2 dla chętnych dla 1 i 2 dodać możliwość podawania wielu liczb do obliczeń. Na innej gałęzi.
    """
if __name__ == "__main__": 
    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ") # Pobiera od użytkownika komendę
    if komenda.lower() == 'help': # Jeśli użytkownik wpisze 'help', wywołaj funkcję help
        help(kalkulator_help) 
# Koniec helpa