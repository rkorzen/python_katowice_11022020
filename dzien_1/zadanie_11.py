x = int(input("Podaj x"))
y = int(input("Podaj y"))


if x < 0 or y < 0 or x > 100 or y > 100:
    print("Poza planszą")
elif x > 90 and y > 90:
    print("PG")
elif x > 90 and y < 10:
    print("DP")
elif x < 10 and y < 10:
    print("DL")
elif x < 10 and y > 90:
    print("GL")
elif x > 90:
    print("PK")
elif x < 10:
    print("LK")
elif y > 90:
    print("GK")
elif y < 10:
    print("DK")
else:
    print("Centrum")