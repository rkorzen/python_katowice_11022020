def sumuj(a, b, *lista):
    print(lista)
    return a + b + sum(lista)


# print(sumuj(1))
print(sumuj(1, 2))
print(sumuj(1, 2, 3))
print(sumuj(1, 2, 3, 5, 10))


def foo(*args, **kwargs):
    print(args)
    print(kwargs)




foo(
    'koszt $cena PLN',
    'kwota $cena brutto',
    'podatek: $podatek %',
    cena=10,
    podatek=20,
)


napis = "$ala ma $kota"
slownik = {"ala": "Ola", "kota":"psa"}
print(slownik)
print(napis)
for k, v in slownik.items():
    print("$"+k)
    napis = napis.replace("$"+k, v)
print(napis)
