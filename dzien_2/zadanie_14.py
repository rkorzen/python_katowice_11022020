#
# liczba_min = None
# if liczba_min is None:
#     print("Tak")
#
# # is True is False is None
# ""
# x = "Napis 1 dfdfdf"
# y = "Napis 1 dfdfdf"
#
# print(id(x), id(y))
#
# x == y
# x is y
liczba_max = None
liczba_min = None

while True:
    polecenie = input("Podja liczbę lub wpisz k by zakończyć: ")
    if polecenie == 'k':
        break
    liczba = int(polecenie)
    if liczba_min is None or liczba < liczba_min:
        liczba_min = liczba
    if liczba_max is None or liczba > liczba_max:
        liczba_max = liczba

if liczba_max is None:
    print("Nie podano liczb")
else:
    print("Maximum: ", liczba_max)
    print("Minimum: ", liczba_min)