# n = 10
# warunek = n % 2 == 0
#
# if warunek:  # True albo False - do tego się sprowadza warunek
#     print("Podzielne")
# else:
#     print("Nieparzyste")
#
# print("Po ifie")
#
# if n % 2 == 0:
#     print("Parzyste")
# elif n % 3 == 0:
#     print("Podzielne przez 3")
# else:
#     print("Pozostałe przypadki")
#
#
import datetime

CURRENT_YEAR = datetime.datetime.now().year

# CURRENT_YEAR = 2020
rok_ur = int(input("Podaj rok urodzenia: "))

if CURRENT_YEAR - rok_ur >= 18:
    print("Jesteś pełnoletni")
else:
    print("Musisz jeszcze poczekać")