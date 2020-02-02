
def przytnij(data, start, stop):
    wynik = []
    dodawaj = False
    for d in data:
        if start(d):
            dodawaj = True
        if dodawaj:
            wynik.append(d)
            if stop(d):
                break
    return wynik


def test_przytnij():
    result = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    )
    assert result == [4, 5, 6]
