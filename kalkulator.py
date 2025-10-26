import sys                                  # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging                              # Importuje moduł logging do obsługi logowania komunikatów
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")    # Ustawia poziom logowania na INFO i logowanie do pliku logfile.log
#logging.basicConfig(level=logging.DEBUG)    # Ustawia poziom logowania na DEBUG

def kalkulator_help():
    """
    Kalkulator wykonujący podstawowe działania matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie.
    Program prosi użytkownika o wybór działania oraz dwie liczby, a następnie wykonuje wybrane działanie i wyświetla wynik.
    Program obsługuje błędy, takie jak nieprawidłowy wybór działania, nieprawidłowe dane wejściowe oraz dzielenie przez zero.
    Wszystkie ważne zdarzenia są logowane do pliku logfile.log.
    + Sprawdza czy podane dane są liczbami.
    + Pozwala na podanie wielu liczb dla dodawania i mnożenia.
    ----------------------------
    Możliwe upgrade'y:
    - Dodanie wyświetlania w wyniku działania pełnego równania (np. 2 + 2 = 4). lub podobne
    - Dodanie mozliwości wykonywania kolejnych działań na wyniku poprzedniego działania bez konieczności ponownego uruchamiania programu.
    - Co wiąże się z opcją wyboru czy użytkownik chce zakończyć działanie programu czy kontynuować z wynikiem poprzedniego działania.
    ----------------------------
    
    """
if __name__ == "__main__":  # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ") # Pobiera od użytkownika komendę
    if komenda.lower() == 'help': # Jeśli użytkownik wpisze 'help', wywołaj funkcję kalkulator_help
        help(kalkulator_help) 

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
        if typ in ('1','3'):
            print("W tej operacji możesz podać więcej niż dwie liczby, oddzielając je SPACJĄ.") # Informuje użytkownika o możliwości podania wielu liczb dla dodawania i mnożenia
            
            more_then_one = input("Podaj liczby: ").split() # Pobiera od użytkownika liczby i dzieli je na listę

            def czy_liczba(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    return False
            if all(czy_liczba(num) for num in more_then_one): # Sprawdza, czy wszystkie wartości są liczbami
                liczby = [float(num) for num in more_then_one] # Konwertuje wszystkie liczby na float
                if typ == '1': # Jeśli user wybrał 1 - Dodawanie:
                    wynik = sum(liczby) # Oblicza sumę wpisanych liczb
                    log_msg = "Suma"

            #dodawanie = input("Podaj liczby: ").split() # Pobiera od użytkownika liczby i dzieli je na listę
            #if all(num.replace('.','',1).isdigit() for num in dodawanie): # Podmienia napotkaną kropkę na brak znaku Sprawdza, czy wszystkie wartości są liczbami (obsługa liczb zmiennoprzecinkowych)
            #    liczby = [float(num) for num in dodawanie] # Konwertuje wszystkie liczby na float
            #    if typ == '1': # Jeśli user wybrał 1 - Dodawanie:
            #        wynik = sum(liczby) # Oblicza sumę wpisanych liczb
            #        log_msg = "Suma"
                else: 
                    typ == '3' # Jeśli user wybrał 3 - Mnożenie:
                    wynik = 1 # Inicjalizuje wynik mnożenia
                    for num in liczby:
                        wynik *= num # Oblicza iloczyn wpisanych liczb
                    log_msg = "Iloczyn"
                logging.info(f'{log_msg} liczb: {", ".join(more_then_one)}') # Loguje informację o wykonywanym działaniu
                if wynik.is_integer():
                    print(f"Wynik dzialania: {int(wynik)}") # Drukuje wynik jako liczbę całkowitą
                    #logging.info("Wynik to %d" % int(wynik)) # Loguje wynik jako liczbę całkowitą
                else:
                    print(f"Wynik to: {wynik:.2f}") # Drukuje wynik jako liczbę zmiennoprzecinkową z dwoma miejscami po przecinku
                logging.info("Wynik to %.2f" % wynik) # Loguje wynik jako liczbę z dwoma miejscami po przecinku
                
                # HELP
                if __name__ == "__main__":
                    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ")
                    if komenda.lower() == 'help': # Jeśli użytkownik wpisze 'help', wywołaj funkcję kalkulator_help
                        help(kalkulator_help)
                # HELP KONIEC

            sys.exit() # Kończy program po wykonaniu działania dla wielu liczb
        break
    else:
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
    logging.error("Podano nieprawidłowy numer działania: %s" % typ) # Loguje błąd nieprawidłowego działania

def czy_liczba(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")
    if czy_liczba(a) and czy_liczba(b):
        a = float(a)
        b = float(b)
        # ... dalsza logika
        break
    else:
        print("Nieprawidłowe dane, możesz wpisać tylko liczby! Spróbuj ponownie.")
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

# HELP
if __name__ == "__main__":
    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ")
    if komenda.lower() == 'help':
        help(kalkulator_help)
 #HELP KONIEC
