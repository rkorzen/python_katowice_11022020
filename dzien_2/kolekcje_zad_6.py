liczby = [5, 2, 1, 4, 3]
# na oko
# i_min = 2
# i_max = 0

# wykorzystanie metod i funkcji pythona
# i_min = liczby.index(min(liczby))
# i_max = liczby.index(max(liczby))

# wykorzystanie podejscia mniej zależnego od jezyka
i_min, i_max = 0, 0
for index, value in enumerate(liczby):
    if value < liczby[i_min]:
        i_min = index
    if value > liczby[i_max]:
        i_max = index


# tmp = liczby[i_min]
# liczby[i_min] = liczby[i_max]
# liczby[i_max] = tmp

liczby[i_min], liczby[i_max] = liczby[i_max], liczby[i_min]
assert liczby == [1, 2, 5, 4, 3]