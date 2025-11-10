import sys #NOWA WERSJA PLIKU
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

def kalkulator_help():
    """
    Kalkulator wykonuje podstawowe działania matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie.
    Pozwala podać wiele liczb dla dodawania i mnożenia.
    Obsługuje błędy i loguje działania.
    """
    print("""
    Kalkulator wykonuje: dodawanie, odejmowanie, mnożenie, dzielenie.
    - Podaj 'help', aby zobaczyć instrukcję.
    - Możesz wykonywać działania na wielu liczbach dla dodawania/mnożenia.
    """)





# Funkcja sprawdzająca, czy dany ciąg znaków jest liczbą
def czy_liczba(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Funkcja pobierająca i walidująca wybór działania od użytkownika
def pobierz_dzialanie():
    dzialania = {
        '1': ('Dodawanie (+)', lambda x, y: x + y, "Suma"),
        '2': ('Odejmowanie (-)', lambda x, y: x - y, "Różnica"),
        '3': ('Mnożenie (*)', lambda x, y: x * y, "Iloczyn"),
        '4': ('Dzielenie (/)', lambda x, y: x / y, "Iloraz"),
    }
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
        logging.error("Podano nieprawidłowy numer działania: %s" % typ)
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
        sys.exit()
    return typ, dzialania

# Funkcja pobierająca liczby od użytkownika w zależności od wybranego działania
# Opis dziłania: jeśłi działanie to dodawanie lub mnożenie, pozwala na podanie wielu liczb oddzielonych spacją
# w przeciwnym razie pobiera dwie liczby
def pobierz_liczby(typ):
    if typ in ['1', '3']:
        wpisane = input("Podaj liczby oddzielone spacją: ").split()
        if all(czy_liczba(num) for num in wpisane):
            liczby = [float(num) for num in wpisane]
            return liczby
        else:
            logging.error("Nieprawidłowe dane: %s" % ", ".join(wpisane))
            print("Nieprawidłowe dane! Możesz wpisać tylko liczby.")
            sys.exit()
    else:
        a = input("Podaj pierwszą liczbę: ")
        b = input("Podaj drugą liczbę: ")
        if czy_liczba(a) and czy_liczba(b):
            return [float(a), float(b)]
        else:
            logging.error("Wpisano nieprawidłowe znaki: %s, %s" % (a, b))
            print("Nieprawidłowe dane! Możesz wpisać tylko liczby.")
            sys.exit()

def wykonaj_dzialanie(typ, dzialania, liczby):
    nazwa, operacja, log_msg = dzialania[typ]
    if typ == '1':
        wynik = sum(liczby)
    elif typ == '3':
        wynik = 1
        for num in liczby:
            wynik *= num
    else:
        wynik = operacja(liczby[0], liczby[1])
    logging.info(f'{log_msg} {", ".join(str(l) for l in liczby)}')
    if wynik.is_integer():
        print(f"Wynik to: {int(wynik)}")
        logging.info("Wynik to %d" % int(wynik))
    else:
        print(f"Wynik to: {wynik:.2f}")
        logging.info("Wynik to %.2f" % wynik)

if __name__ == "__main__":
    komenda = input("\nWpisz 'help' aby zobaczyć instrukcję, lub ENTER aby kontynuować: ")
    if komenda.lower() == 'help':
        kalkulator_help()
    typ, dzialania = pobierz_dzialanie()
    liczby = pobierz_liczby(typ)
    wykonaj_dzialanie(typ, dzialania, liczby)
