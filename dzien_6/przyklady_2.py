

class Pojazd:

    def __init__(self, nazwa):
        self.nazwa = nazwa

    def poruszaj_sie(self):
        print("Porusza sie")

    def stop(self):
        print("Pojazd zatrzymal się")

class Statek(Pojazd):

    def plyn(self):
        self.poruszaj_sie()
        print("Płynie ...")

class Samochod(Pojazd):

    def jedz(self):
        self.poruszaj_sie()
        print("Jedzie ...")

class Amfibia(Statek, Samochod):

    def __init__(self, nazwa, typ):
        super().__init__(nazwa)
        # Statek.__init__(self, nazwa)
        self.typ = typ

prom = Statek("Batory")
prom.plyn()
prom.stop()

samochod = Samochod("Ford")
samochod.jedz()
samochod.stop()

amfibia = Amfibia("Lola", "Wojskowa")
amfibia.jedz()
amfibia.plyn()
amfibia.stop()
#######

# metody klasowe
import datetime
class Osoba:

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def osoba_z_rok_ur(cls, imie, rok_ur):
        wiek = datetime.datetime.now().year - rok_ur
        return cls(imie, wiek)

    # @staticmethod
    # def osoba_z_rok_ur(imie, rok_ur):
    #     wiek = datetime.datetime.now().year - rok_ur
    #     return Osoba(imie, wiek)


def osoba_z_rok_ur(imie, rok_ur):
    wiek = datetime.datetime.now().year - rok_ur
    return Osoba(imie, wiek)

os = Osoba("Anna", 25)
os2 = osoba_z_rok_ur("Ala", 1975)
print(os2.wiek)

os3 = Osoba.osoba_z_rok_ur("Marta", 2012)



class Kwadrat:

    def __init__(self, bok):
        self.bok = bok

    @property
    def obwod(self):
        return self.bok * 4

    @obwod.setter
    def obwod(self, ob):
        self.bok = ob / 4

kw = Kwadrat(4)
print(kw.obwod)
kw.obwod = 20
assert kw.bok == 5