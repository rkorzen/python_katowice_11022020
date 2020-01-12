# ctr alt l
# x = 0
# f"ala ma kota {x} : "
i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1  # i = i + 1

print("=" * 40)

while i > 0:
    print(i)
    i = i - 1
    if i == 6:
        print("przerywam petle")
        break

print("linia po petli")
