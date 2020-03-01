import json
source_format = "json"  # "csv"

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

def odczytaj_dane(format):
    if format == "json":
        try:
            with open("pracownicy.json") as f:
                dane = json.load(f)
        except FileNotFoundError:
            dane = []
    else:
        raise NotImplementedError("Ten format nie jest obsługiwany")
    return dane

def zapisz_dane(format):
    if format == "json":
        with open("pracownicy.json", "w") as f:
            json.dump(pracownicy, f)
    else:
        raise NotImplementedError("Nieobsługiwany format")
    print("Dane zapisano!")


pracownicy = odczytaj_dane(source_format)
polecenie = input("Co chcesz zrobić? [d-dodać, w-wypisać]")

if polecenie == 'd':
    pracownicy = dodaj_pracownika(pracownicy)

    zapisz_dane(pracownicy)
elif polecenie == "w":
    wypisz_pracownikow(pracownicy)