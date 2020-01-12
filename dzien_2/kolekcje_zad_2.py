"""
Celem zadania...

"""
lista = []

while len(lista) < 10:
    polecenie = input("Wpisz liczbę, lub k by zakończyć: ") # to jest ignorowane
    if polecenie == "k":
        break
    try:
        liczba = int(polecenie)
        lista.append(liczba)
    except ValueError:
        print("wpisane coś co nie jest liczbą!!")

print(f"wartość średnia wynosi {sum(lista)/len(lista):.3f}")