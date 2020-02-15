import datetime

class Osoba:
    gatunek = "Homo Sapiens"

    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    def podaj_wiek(self):
        return datetime.datetime.now().year - self.rok_ur

    def __str__(self):
        return f"<Osoba {self.imie}>"

os1 = Osoba("Rafał", 1980)
os2 = Osoba("Ania", 1990)

Osoba.gatunek = "Kosmita"
os1.gatunek = "Człowiek rozumny"
print(os1.gatunek)
print(os2.gatunek)