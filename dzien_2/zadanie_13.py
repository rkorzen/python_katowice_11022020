
DNI_TYGODNIA = 7
i = 0
suma_temp = 0

while i < DNI_TYGODNIA:
    temperatura = int(input("Podaj temperaturę: "))
    suma_temp += temperatura
    i += 1

print(f"Średnia temperatura wynosi: {suma_temp / DNI_TYGODNIA:.2f}")