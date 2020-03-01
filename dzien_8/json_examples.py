import json

lista = [1, 2, 3]
slownik = {'ala': 'kot', 'lista': lista}

# print(json.dumps(slownik))
with open("dane2.json", 'w') as f:
    json.dump(slownik, f)

with open("dane.json") as f:
    dane = json.load(f)

print(dane)
