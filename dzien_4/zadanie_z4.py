
def formatuj(*args, **kwargs):
    text = "\n".join(args)
    for slowo, wartosc in kwargs.items():
        klucz = "$"+slowo
        text = text.replace(klucz, wartosc)
    return text


def test_formatuj():
    assert formatuj("ala $ma kota") == "ala $ma kota"
    assert formatuj("ala $ma kota", "kot ma Alę") == "ala $ma kota\nkot ma Alę"
    assert formatuj("ala $ma $kota", ma="miała", kota="psa") == "ala miała psa"
    assert formatuj("ala $ma $kota") == "ala $ma $kota"


    # foo(
    #     'koszt $cena PLN',
    #     'kwota $cena brutto',
    #     'podatek: $podatek %',
    #     cena=10,
    #     podatek=20,
    # )