lista = [10, 20, 30]
potegi = [2, 3, 2]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

for zmienna_pomocnicza in lista:
    print(zmienna_pomocnicza)
print("xx", zmienna_pomocnicza)
# for i in range(100):
#     print(i)
for i, v in enumerate(lista):
    print(i, v)

for i, v in enumerate(lista):
    print(v ** potegi[i])

for wartosc, potega in zip(lista, potegi):
    print(wartosc**potega)

a = 1
b = 2

c, d = 10, 12