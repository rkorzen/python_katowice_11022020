DEVELOPMENT =True

zliczenia = {}


if DEVELOPMENT:
    text = "ALA ma kota"
else:
    text = input("Wpisz tekst: ")

# ver 1
for znak in text:
    if znak in zliczenia:
        zliczenia[znak] += 1
    else:
        zliczenia[znak] = 1

# ver 2
for znak in text:
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

# ver 3
from collections import defaultdict

zliczenia = defaultdict(int)
for znak in text.lower():
    zliczenia[znak] += 1

print(zliczenia)