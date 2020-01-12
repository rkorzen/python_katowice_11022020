# 01_typy_liczbowe.py
# plik pythonowy nazywamy modulem.

# liczby calkowite - int
# funkcj do sprawdzania typu:
print(type(1))

# uruchomienie skryptu/ modulu:
# python nazwa_modulu.py

# operacje i operatory 
print(1 + 1)
print(1 - 1)
print(1 * 2)
print(1 / 2)  
print(1 // 2)
# print(10 / 0)
print(10 % 3)
print(2**3)
print(pow(2, 3))

print(3 > 4)
print( 4 == 2*2)
# > >= < <= == !=

# wartosci logiczne
True
False

print(type(True))
print(bool())

print(bool(10))
print(bool("a"))
print(bool(""))

print(1 + True) 

print(1_000_000) 
print(1000000)
print(0b101010)
print(0o1234567)
print(0x123456789abcdef)

# zmienne
nazwa_zmiennej = "wartosc" 
# nazwaZmienne, NazwaZmienej
# nie moga sie zaczynac od cyfr
# moga sie skladac tylko z liczb liter i znaku podkreslenia
# nie moze to byc tez slowo kluczowe

_ = 10

# konwencja - stale
X = 10

# liczby zmienno przecinkowe
0.11

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))

float()
'float'

complex()
'complex'



