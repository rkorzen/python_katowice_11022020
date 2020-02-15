import datetime

class Osoba:
    def __init__(self, imie, rok_ur):
        self.imie = imie
        self.rok_ur = rok_ur

    def podaj_wiek(self):
        return datetime.datetime.now().year - self.rok_ur

    def __str__(self):
        return f"<Osoba {self.imie}>"

os1 = Osoba("Rafał", 1980)
print(os1.podaj_wiek())
print(Osoba.podaj_wiek(os1))

print(os1)
os2 = Osoba("Ania")
print(os2)
print(dir(os1))
print(type(os1))

print(os1.imie)

