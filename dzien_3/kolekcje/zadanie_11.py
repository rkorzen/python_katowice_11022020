
liczby = set()

while True:
    polecenie = input("Wprowadź liczbę lub k by zakończyć")
    if polecenie == 'k':
        break
    liczby.add(int(polecenie))

parzyste = set(range(0, 101, 2))
print(f"""
Liczb unikalnych: {len(liczby)}
W tym parzystych z przedziału 0-100: {len(liczby & parzyste)}
""")