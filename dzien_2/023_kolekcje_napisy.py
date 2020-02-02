napis = "Ala ma kota"
SAMOGLOSKI = "aeiouy"

licznik = 0
for litera in napis.lower():
    if litera in SAMOGLOSKI:
        licznik += 1

print("Samogłosek: ", licznik)

# "A" in napis
napis[1:]

