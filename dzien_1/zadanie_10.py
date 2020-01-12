# + - / *

liczba1 = int(input("Podaj liczbe 1: "))
liczba2 = int(input("Podaj liczbe 2: "))
operacja = int(input("Działanie: "))

if operacja == "+":
    wynik = liczba1 + liczba2
elif operacja == '-':
    wynik = liczba1 - liczba2
elif operacja == "*":
    wynik = liczba1 * liczba2
elif operacja == "/":
    # ask  for permission
    if liczba2 == 0:
        wynik = "Pamietaj cholero nie dziel przez zero"
    else:
        wynik = liczba1 / liczba2

    # # beg for forgivenes
    # try:
    #     wynik = liczba1 / liczba2
    # except ZeroDivisionError:
    #     wynik = "Pamietaj cholero nie dziel przez zero"
else:
    wynik = "Nieznana operacja"

print(wynik)