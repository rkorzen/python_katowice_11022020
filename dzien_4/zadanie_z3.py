

def policz_znaki(text, start="<", stop=">"):
    wynik = 0
    poziom = 0
    for znak in text:
        if znak == start:
            poziom += 1
        elif znak == stop:
            poziom -= 1
        else:
            wynik += poziom
    return wynik


def test_policz_znaki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6
