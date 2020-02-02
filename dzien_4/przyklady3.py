def tabliczka(x, y):
    wynik = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i*j)
        wynik.append(row)
    return wynik

def tabliczka2(x, y):
    return [[i*j for i in range(x)] for j in range(y)]

def printuj(tabliczka):
    for row in tabliczka:
        print(row)


printuj(tabliczka2(6, 6))
