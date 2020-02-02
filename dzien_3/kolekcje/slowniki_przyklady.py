x = [1, 2]
# pary wartosci
# key: value
# rozdzielone przecinkiem
# key - unikalna wartość, hashowalna (najczęściej niemutowalna)
# value - to w zasadzie dowolny obiekt

pol_ang = {
    "kot": "cat",
    "pies": "dog",
}
print(pol_ang)
pol_ang = dict(kot="cat", pies="dog")
print(pol_ang)
pol_ang = dict([("kot", "cat"),("pies", "dog")])
print(pol_ang)
pol_ang["kaczka"] = "duck"
print(pol_ang)
pol_ang["kaczka"] = "a duck"

# slownik[klucz] = wartosc
print(pol_ang)
print(pol_ang["kot"])

# print(pol_ang["cat"])
if "jaszczurka" in pol_ang:
    print(pol_ang["jaszczurka"])

print(pol_ang.get("jaszczurka"))
print(pol_ang.get("jaszczurka", "Brak hasła"))

print(pol_ang.get(None, "Brak"))

print(dir(pol_ang))
# 'clear', 'copy', 'fromkeys',
# 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values'


"3,6".replace(",", ".")

for k in pol_ang:
    print(k, pol_ang[k])

ilosci = {
    "k": 1000
}

x = {}
x = dict()

print(type(ilosci['k']))

a, b = 1, 2
print(pol_ang.items())
for k, v in pol_ang.items(): #
    print(k, v)


print(len(pol_ang))

print(sorted(pol_ang.items()))