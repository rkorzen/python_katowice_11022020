import random

DEBUG = False

WYMIAR_PLANSZY = 10

gracz_x = random.randint(1, WYMIAR_PLANSZY)
gracz_y = random.randint(1, WYMIAR_PLANSZY)

skarb_x = random.randint(1, WYMIAR_PLANSZY)
skarb_y = random.randint(1, WYMIAR_PLANSZY)

odl_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
liczba_krokow = 0
while True:
    odl_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if DEBUG:
        print(f"g_x, g_y =  {gracz_x}, {gracz_y}")
        print(f"s_x, s_y =  {skarb_x}, {skarb_y}")

    ruch = input("W którą stronę? (gdlp): ")
    if ruch == "g":
        gracz_y += 1
    elif ruch == "d":
        gracz_y -= 1
    elif ruch == 'l':
        gracz_x -= 1
    elif ruch == 'p':
        gracz_x += 1
    if gracz_x < 1 or gracz_x > WYMIAR_PLANSZY or gracz_y > WYMIAR_PLANSZY or gracz_y < 1:
        print("Jesteś poza planszą")
        break
    odl_po = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    liczba_krokow += 1
    if odl_po == 0:
        if liczba_krokow > 1:
            msg = f"Wygrana! (W {liczba_krokow}) krokach"
        else:
            msg = f"Wygrana! (W {liczba_krokow}) kroku!!! Wow!"
        print(msg)
        break

    if liczba_krokow > odl_po_wylosowaniu * 2:
        print("Jesteś gapa. Skarb zmienia położenie!!! ")
        liczba_krokow = 0
        skarb_x = random.randint(1, WYMIAR_PLANSZY)
        skarb_y = random.randint(1, WYMIAR_PLANSZY)
        odl_po_wylosowaniu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    else:
        if random.randint(1, 5) != 2:
            if odl_przed > odl_po:
                print("Ciepło")
            else:
                print("Zimno")

print("Koniec!!")
