import json
import csv

from sqlite_example import create_connection, execute_query, execute_read_query, create_pracownik_sql, select_pracownicy

source_format = "sql"  # "csv"


def wypisz_pracownikow(pracownicy):
    for i, pracownik in enumerate(pracownicy, start=1):
        print(
            f" - [{i}] {pracownik['imie']} {pracownik['nazwisko']} - rok: "
            f"{pracownik['rok_ur']}, pensja: {pracownik['pensja']}"
        )


def dodaj_pracownika(pracownicy):
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    rok_ur = int(input("Podaj rok urodzenia: "))
    pensja = float(input("Podaj pensję: "))

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_ur": rok_ur,
        "pensja": pensja
    }

    pracownicy.append(pracownik)
    return pracownicy


def read_json():
    try:
        with open("pracownicy.json") as f:
            dane = json.load(f)
    except FileNotFoundError:
        dane = []
    return dane


def read_csv():
    dane = []
    try:
        with open("pracownicy.csv") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                dane.append(row)
    except FileNotFoundError:
        pass
    return dane


def read_sql():
    query_sql = "SELECT imie, nazwisko, rok_ur, pensja FROM pracownicy"
    with create_connection("pracownicy.sqlite") as connection:
        dane = execute_read_query(connection, query_sql)
    dane_as_dicts = []
    for d in dane:
        dane_as_dicts.append({"imie": d[0], "nazwisko": d[1], "rok_ur": d[2], "pensja": d[3]})
    return dane_as_dicts


def odczytaj_dane(format):
    if format == "json":
        dane = read_json()
    elif format == "csv":
        dane = read_csv()
    elif format == "sql":
        dane = read_sql()
    else:
        raise NotImplementedError("Ten format nie jest obsługiwany")
    return dane


def to_json(dane):
    with open("pracownicy.json", "w") as f:
        json.dump(dane, f)


def to_csv(dane):
    with open("pracownicy.csv", "w", newline="") as f:
        fieldnames = ["imie", "nazwisko", "rok_ur", "pensja"]
        writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
        writer.writeheader()
        for row in dane:
            writer.writerow(row)


def to_sql(dane):
    pracownik = dane[-1]
    with create_connection("pracownicy.sqlite") as connection:
        sql = create_pracownik_sql(pracownik.values())
        execute_query(connection, sql)


def zapisz_dane(format, dane):
    if format == "json":
        to_json(dane)
    elif format == "csv":
        to_csv(dane)
    elif format == "sql":
        to_sql(dane)
    else:
        raise NotImplementedError("Nieobsługiwany format")
    print("Dane zapisano!")


pracownicy = odczytaj_dane(source_format)
polecenie = input("Co chcesz zrobić? [d-dodać, w-wypisać]")

if polecenie == 'd':
    pracownicy = dodaj_pracownika(pracownicy)
    zapisz_dane(source_format, pracownicy)
elif polecenie == "w":
    wypisz_pracownikow(pracownicy)
