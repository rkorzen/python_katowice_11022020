# Tupla, krotka

krotka = (1, 2.0, 'ala', (4, 5), 1)
# 0, 1,   2,     3,      4
print(dir(krotka))
#  'count', 'index'

print(krotka.count('ala'))
print(krotka.count(1))
print(krotka.index(1))
print(krotka.index('ala'))
# print(krotka.index('xxxx'))
print(help(krotka.index))

print("Zwracana wartosc", krotka[2])
print("Zwracana wartosc", krotka[-1])
print("Zwracana wartosc", krotka[1:-1])
print("Zwracana wartosc", krotka[:-1])
print("Zwracana wartosc", krotka[1:])
print("Zwracana wartosc", krotka[::2])  # od poczatku do konca co drugi
print("Zwracana wartosc", krotka[::-1])

k1 = (1, 2, 3)
k2 = (4, 5, 6)

print(k1 + k2)
print(tuple())
print((1,))
