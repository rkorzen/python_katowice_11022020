miasto_a = input("Podaj miasto A: ")
miasto_b = input("Podaj miasto B: ")
dystans = int(
   input(f"Dystans na trasie {miasto_a}-{miasto_b}: ")
)
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

print()
koszt = dystans * spalanie * cena / 100

print(f"Koszt przejazdu {miasto_a}-{miasto_b} to {koszt:.2f} PLN")