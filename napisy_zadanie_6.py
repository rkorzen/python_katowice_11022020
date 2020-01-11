
try:
	liczba = int(input("Podaj liczbę: "))
    print()
	print(f"Większa od 10 { liczba > 10 }")
	print(f"Mniejsza, równa 15 { liczba <= 15 }")
	print(f"Podzielna przez dwa { liczba % 2 == 0}")
except:
    print("Coś się nie powiodło")
