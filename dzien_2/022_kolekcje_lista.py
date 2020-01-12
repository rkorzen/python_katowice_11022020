# Tupla, krotka

lista = [1, 2.0, 'ala', (4, 5), 1]
# 0, 1,   2,     3,      4
print(dir(lista))
#   'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(lista.count('ala'))
print(lista.count(1))
print(lista.index(1))
print(lista.index('ala'))
# print(krotka.index('xxxx'))
print(help(lista.index))

print("Zwracana wartosc", lista[2])
print("Zwracana wartosc", lista[-1])
print("Zwracana wartosc", lista[1:-1])
print("Zwracana wartosc", lista[:-1])
print("Zwracana wartosc", lista[1:])
print("Zwracana wartosc", lista[::2])  # od poczatku do konca co drugi
print("Zwracana wartosc", lista[::-1])

k1 = [1, 2, 3]
k2 = [4, 5, 6]

print(k1 + k2)
print(list())
print([1])


xxx = []
print(xxx)

xxx.append(10)
print(xxx)

lista = [1, 2, 3, 4, 5]
lista.insert(1, 10)

print(lista)