import time

N = 10
# start = time.time()
# wynik = []
# for el in range(N):
#     if el % 2 == 0:
#         wynik.append(el**3)
# print(time.time() - start)
#
# start = time.time()
# [(el, el**3) for el in range(N) if el % 2 == 0]
print({el: el**3 for el in range(N) if el % 2 == 0})
print({el**3 for el in range(N) if el % 2 == 0})
print((el**3 for el in range(N) if el % 2 == 0))
# print(time.time() - start)
#
# import dis
# print(dis.dis("""
# for el in range(N):
#     if el % 2 == 0:
#         wynik.append(el**3)
# """))
#
# print(dis.dis('''[(el, el**3) for el in range(N) if el % 2 == 0]'''))


# liste zawierajaca liczby zmiennoprzecinkowe od 0.0 do 1.0 z
# krokiem 0.1

print([i/10 for i in range(0, 11)])
# I zbiór tupli zawierajacych 3 elementy - dana liczbe, jej kwadrat i
# jej szescian - w przedziale od -10 do 10

print({(i, i**2, i**3) for i in range(-10, 10)})
# I słownik mapujacy napisy na ich długosc powstały ze zbioru
# napisów
napisy = set(['aaa','aaaaa','aaaaaaaaaaa'])

print({napis: len(napis) for napis in napisy})
