# to jest plik 2_kalkulator.py - alternatywna wersja kalkulatora 
# zmiany zasugerowane przez AI na podstawie mojego oryginalnego pliku kalkulator.py
# Program obsługuje błędy, takie jak nieprawidłowy wybór działania, nieprawidłowe dane wejściowe oraz dzielenie przez zero.
# Wszystkie ważne zdarzenia są logowane do pliku logfile.log.
# Nie dodawałem tutaj funkcji help, ponieważ nie jest to kluczowe dla działania kalkulatora a jest to moja rozszerzona wersja oryginalnego pliku kalkulator.py
#gdzie chciałem zobaczyć jak to się konstruuje.

import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', filename="logfile.log")

dzialania = {
    '1': ('Dodawanie (+)', "Suma"),
    '2': ('Odejmowanie (-)', "Różnica"),
    '3': ('Mnożenie (*)', "Iloczyn"),
    '4': ('Dzielenie (/)', "Iloraz"),
}

def czy_liczba(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print("""Jakie działanie chcesz wykonać:
1 - Dodawanie (+)
2 - Odejmowanie (-)
3 - Mnożenie (*)
4 - Dzielenie (/)
""")

while True:
    typ = input("Podaj numer działania (1/2/3/4): ")
    if typ in dzialania:
        print("Wybrano:", dzialania[typ][0])
        break
    else:
        print("Nieprawidłowy wybór, podaj liczbę od 1 do 4.")
        logging.error("Podano nieprawidłowe działanie: %s" % typ)

if typ in ('1', '3'):  # Dodawanie i Mnożenie dla wielu liczb
    print("W tej operacji możesz podać więcej niż dwie liczby, oddzielając je spacją.")
    liczby_s = input("Podaj liczby: ").split()
    if all(czy_liczba(num) for num in liczby_s):
        liczby = [float(num) for num in liczby_s]
        if typ == '1':
            wynik = sum(liczby)
            log_msg = "Suma"
        else:  # typ == '3'
            wynik = 1
            for num in liczby:
                wynik *= num
            log_msg = "Iloczyn"
        logging.info(f'{log_msg} liczb: {", ".join(liczby_s)}')
        if wynik.is_integer():
            print(f"Wynik działania to {int(wynik)}")
            logging.info("Wynik to %d" % int(wynik))
        else:
            print(f"Wynik to {wynik:.2f}")
            logging.info("Wynik to %.2f" % wynik)
        sys.exit()
    else:
        print("Nieprawidłowe dane, wpisz tylko liczby!")
        logging.error("Wpisano nieprawidłowe znaki: %s" % ", ".join(liczby_s))
        sys.exit()

# dla odejmowania/dzielenia (dokładnie dwie liczby)
while True:
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")
    if czy_liczba(a) and czy_liczba(b):
        a = float(a)
        b = float(b)
        if typ == '4' and b == 0:
            print("Nie można dzielić przez zero, podaj drugą liczbę różną od 0.")
            logging.error("Próba dzielenia przez zero.")
            continue
        break
    else:
        print("Nieprawidłowe dane, możesz wpisać tylko liczby! Spróbuj ponownie.")
        logging.error("Wpisano nieprawidłowe znaki: %s, %s" % (a, b))

# wykonanie działania
if typ == '2':  # odejmowanie
    wynik = a - b
    log_msg = "Różnica"
else:           # typ == '4' dzielenie
    wynik = a / b
    log_msg = "Iloraz"

logging.info(f'{log_msg} {a:.2f} i {b:.2f}')
print(f"{log_msg} {a:.0f} i {b:.0f}")
if wynik.is_integer():
    print(f"Wynik to {int(wynik)}")
    logging.info("Wynik to %d" % int(wynik))
else:
    print(f"Wynik to {wynik:.2f}")
    logging.info("Wynik to %.2f" % wynik)
