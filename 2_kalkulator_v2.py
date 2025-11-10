import sys      # Importuje moduł sys do obsługi argumentów wiersza poleceń
import logging  # Importuje moduł logging do obsługi logowania komunikatów

# Ustawia poziom logowania na INFO i logowanie do pliku logfile.log
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

# ========== Funkcje pomocnicze (POCZĄTEK) ==========

def kalkulator_help():
    """
Kalkulator wykonujący podstawowe działania matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie.
Program prosi użytkownika o wybór działania oraz dwie liczby, a następnie wykonuje wybrane działanie i wyświetla wynik.
Program obsługuje błędy, takie jak nieprawidłowy wybór działania, nieprawidłowe dane wejściowe oraz dzielenie przez zero.
Wszystkie ważne zdarzenia są logowane do pliku logfile.log.
+ Sprawdza czy podane dane są liczbami.
+ Pozwala na podanie wielu liczb dla dodawania i mnożenia.
----------------------------
Pomysły na możliwe upgrade'y:
- Dodanie wyświetlania w wyniku działania pełnego równania (np. 2 + 2 = 4). lub podobne
- Ma te także sens w dodawaniu ponieważ można podać tylko jedną liczbę i domyślnie dodaje zero czego nie widać.
- Dodanie mozliwości wykonywania kolejnych działań na wyniku poprzedniego działania bez konieczności ponownego uruchamiania programu.
- Co wiąże się z opcją wyboru czy użytkownik chce zakończyć działanie programu czy kontynuować po wyświetleniu wyniku poprzedniego działania.
- a także po podaniu nieprawidłowej operacji do wykonania program mógłby zapytać czy użytkownik chce spróbować ponownie zamiast kończyć działanie programu.
----------------------------

    """

# Funkcja sprawdzająca, czy dany ciąg znaków jest liczbą

def czy_liczba(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
# Funkcja pobierająca i walidująca wybór działania od użytkownika
# Wyświetla menu działań i prosi użytkownika o wybór

def pobierz_typ_dzialania(dzialania):
    print("""Jakie działanie chcesz wykonać:
1 - Dodawanie (+)
2 - Odejmowanie (-)
3 - Mnożenie (*)
4 - Dzielenie (/)
""")
   
    typ = input("Podaj numer działania (1/2/3/4): ") # Pobiera od użytkownika wybór działania
    if typ in dzialania:
        print("Wybrano:", dzialania[typ][0])
    else:
        logging.error("Podano nieprawidłowy numer działania: %s" % typ) # Loguje błąd nieprawidłowego wyboru
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
        sys.exit()
    return typ

# Funkcja obsługująca pobieranie wielu liczb dla dodawania i mnożenia
# Jeśli użytkownik wybrał dodawanie lub mnożenie, pozwala na podanie wielu liczb oddzielonych spacją

def obsluga_list_liczb(typ): # tu nie kumam dlaczego przekazuję typ działania skoro nie przekazuję go dalej, ale bez tego nie działa..? - do sprawdzenia
    print("W tej operacji możesz podać więcej niż dwie liczby, oddzielając je SPACJĄ.")
    more_then_one = input("Podaj liczby: ").split()
    if all(czy_liczba(num) for num in more_then_one): # Sprawdza czy wszystkie wpisane wartości są liczbami
        liczby = [float(num) for num in more_then_one] # Konwertuje wpisane wartości na liczby zmiennoprzecinkowe
        return liczby, more_then_one
    else:
        print("Nieprawidłowe dane, możesz wpisać tylko liczby! Spróbuj ponownie.")
        logging.error("Wpisano nieprawidłowe znaki: %s" % ", ".join(more_then_one))
        sys.exit()

# ========== Funkcje pomocnicze (KONIEC) ==========


# ========== Słownik działań (POCZĄTEK) ==========

dzialania = {
    '1': ('Dodawanie (+)', lambda x, y: x + y, "Suma"),
    '2': ('Odejmowanie (-)', lambda x, y: x - y, "Różnica"), 
    '3': ('Mnożenie (*)', lambda x, y: x * y, "Iloczyn"),
    '4': ('Dzielenie (/)', lambda x, y: x / y, "Iloraz"),
}
# ========== Słownik działań (KONIEC) ==========


# ========== Main Program/Logika główna (START) ==========

if __name__ == "__main__":  # Sprawdza, czy skrypt jest uruchamiany bezpośrednio
    
    # --- Sekcja: help ---
    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ")
    if komenda.lower() == 'help':
        help(kalkulator_help)

    # --- Sekcja: Pobieranie typu działania ---
    typ = pobierz_typ_dzialania(dzialania)

    # --- Sekcja: Logika dodawania i mnożenia ---
    if typ in ('1','3'):
        liczby, more_then_one = obsluga_list_liczb(typ)

        if typ == '1': # Dodawanie
            wynik = sum(liczby)
            log_msg = "Suma"
        else: # typ == '3' Mnożenie
            wynik = 1
            for num in liczby:
                wynik *= num
            log_msg = "Iloczyn"

        logging.info(f'{log_msg} liczb: {", ".join(more_then_one)}')
        if wynik.is_integer():
            print(f"Wynik dzialania: {int(wynik)}")
        else:
            print(f"Wynik to: {wynik:.2f}")
        logging.info("Wynik to %.2f" % wynik)
        sys.exit()

    # --- Sekcja: Logika odejmowania i dzielenia ---
    while True:
        a = input("Podaj pierwszą liczbę: ")
        b = input("Podaj drugą liczbę: ")
        if czy_liczba(a) and czy_liczba(b):
            a = float(a)
            b = float(b)
            break
        else:
            print("Nieprawidłowe dane, możesz wpisać tylko liczby! Spróbuj ponownie.")
            logging.error("Wpisano nieprawidłowe znaki: %s, %s" % (a, b))

    nazwa, operacja, log_msg = dzialania[typ]
    logging.info(f'{log_msg} {a:.2f} i {b:.2f}')
    print(f"{log_msg} {a:.0f} i {b:.0f}")
    wynik = operacja(a, b)
    if wynik.is_integer():
        print(f"Wynik to {int(wynik)}")
        logging.info("Wynik to %d" % int(wynik))
    else:
        print(f"Wynik to {wynik:.2f}")
        logging.info("Wynik to %.2f" % wynik)

# ========== Main Program/Logika główna (KONIEC) ==========

