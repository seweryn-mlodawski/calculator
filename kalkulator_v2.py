import logging #importuje moduł logowania

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    filename="logfile.log"
)

# Słownik działań
OPERATIONS = {
    '1': ('Dodawanie (+)', lambda x, y: x + y, "Suma"),
    '2': ('Odejmowanie (-)', lambda x, y: x - y, "Różnica"),
    '3': ('Mnożenie (*)', lambda x, y: x * y, "Iloczyn"),
    '4': ('Dzielenie (/)', lambda x, y: x / y, "Iloraz"),
}

# Funkcja do pobierania i walidacji wyboru działania
def get_operation():
    """
    Pobiera i waliduje wybór operacji od użytkownika.
    
    Zwraca:
        str: klucz operacji ('1', '2', '3' lub '4')
    """
    print("""
Jakie działanie chcesz wykonać:
1 - Dodawanie (+)
2 - Odejmowanie (-)
3 - Mnożenie (*)
4 - Dzielenie (/)
""")
    
    while True:
        typ = input("Podaj numer działania (1/2/3/4): ")
        if typ in OPERATIONS:
            print(f"Wybrano: {OPERATIONS[typ][0]}")
            return typ
        else:
            print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
            logging.error(f"Podano nieprawidłowe działanie: {typ}")

# Funkcja do pobierania i walidacji liczb
def get_numbers():
    """
    Pobiera i waliduje dwie liczby od użytkownika.
    
    Zwraca:
        tuple: (liczba1, liczba2) jako float
    """
    while True:
        a = input("Podaj pierwszą liczbę: ")
        b = input("Podaj drugą liczbę: ")
        
        # Sprawdza, czy obie wartości są liczbami (całkowitymi lub zmiennoprzecinkowymi)
        if a.replace('.', '', 1).replace('-', '', 1).isdigit() and \
           b.replace('.', '', 1).replace('-', '', 1).isdigit():
            return float(a), float(b)
        else:
            print("Nieprawidłowe dane, możesz wpisać tylko liczby! Spróbuj ponownie.")
            logging.error(f"Wpisano nieprawidłowe znaki: {a}, {b}")

# Funkcja do wykonywania obliczeń
def calculate(typ, a, b):
    """
    Wykonuje wybrane działanie matematyczne.
    
    Argumenty:
        typ (str): klucz operacji
        a (float): pierwsza liczba
        b (float): druga liczba
        
    Zwraca:
        float: wynik operacji
    """
    nazwa, operacja, log_msg = OPERATIONS[typ]
    
    # Ochrona przed dzieleniem przez zero
    if typ == '4' and b == 0:
        print("Nie można dzielić przez zero, podaj drugą liczbę różną od 0.")
        logging.error("Próba dzielenia przez zero.")
        return None
    
    wynik = operacja(a, b)
    logging.info(f'{log_msg} {a:.2f} i {b:.2f}')
    print(f"{log_msg} {a:.2f} i {b:.2f}")
    
    return wynik

# Funkcja do wyświetlania wyniku
def display_result(wynik):
    """
    Wyświetla wynik w odpowiednim formacie.
    
    Argumenty:
        wynik (float): wynik do wyświetlenia
    """
    if wynik is None:
        return
    
    if isinstance(wynik, float) and wynik.is_integer():
        print(f"Wynik to {int(wynik)}")
        logging.info(f"Wynik to {int(wynik)}")
    else:
        print(f"Wynik to {wynik:.2f}")
        logging.info(f"Wynik to {wynik:.2f}")

# Główna funkcja programu - uruchamia kalkulator
def main():
    """
    Główna funkcja programu - uruchamia kalkulator.
    """
    typ = get_operation()
    
    while True:
        a, b = get_numbers()
        wynik = calculate(typ, a, b)
        
        if wynik is not None:
            display_result(wynik)
            break
        else:
            print("Spróbuj ponownie z inną liczbą.\n")

# Uruchomienie programu
if __name__ == "__main__":
    main()
