ceny = {
    'ziemniaki': 2.99,
    'ogorki': 6.59,
    'pomidory': 5.29
}

w_magazynie = {
    'ziemniaki': 10,
    'ogorki': 10,
    'pomidory': 10
}

while True:
    sciezka = input("Zakup [z]?, Magazyn [m], ")

    if sciezka == "z":
        print("Witaj w naszym sklepie! Oferujemy: ")
        for produkt, cena in ceny.items():
            print(f" - {produkt} - {cena} PLN")

        co = input("Co chcesz kupić? ")
        cena = ceny.get(co)
        if not cena:
            print("Takiego produktu nie oferujemy!")
        else:
            ile = float(input(f"Ile chcesz kupić [{co}]"))
            koszt = cena * ile
            print(f"Należy się: {koszt}")
    elif sciezka == 'm':
        co = input("Co chcesz dodać/uaktualnić? ")
        ile = int(input(f"Ile dodajesz [{co}]? "))
        cena = input(f"Jaka cena za [{co}] (enter by pominąć)? ")

        w_magazynie[co] = w_magazynie.get(co, 0) + ile
        if cena:
            ceny[co] = float(cena)
    else:
        print("Dziękujemy")

