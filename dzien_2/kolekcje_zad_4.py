
liczby = []

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        liczby.append(i)

print("Liczby podzielne przez 3 lub 5: \n")
# [str(x) for x in liczby]  # lista składana, wyrażenie listowe
print("\n".join(map(str, liczby)))
# print("\n".join([str(x) for x in liczby] ))
# wprost
nowa = []
for el in liczby:
    nowa.append(str(el))
# # map
# nowa = list(map(str, liczby))
# # wyrażenie listowe
# nowa = [str(x) for x in liczby]

print(f"W przedziale 0-100 jest {len(liczby)} liczb podzielnych przez 3 lub 5.")