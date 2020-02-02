"""
Napisz funkcję, która sprwdzi, czy tekst jest palindromem
tzn czy czytany wspak jest taki sam jak czytany od początku

Zacznij od prostych palindromów jak ala, kajak
a potem spróbuj czegoś ze spacjami, przecinkami itd

palindrome("kajak") -> True
palindrome("Kajak") -> True

palindrome("A to idiota") -> True

"""
import string


def palindrome(text):
    text = text.lower()
    for s in string.punctuation + string.whitespace:
        text = text.replace(s, "")
    return text == text[::-1]


def test_palindrome():
    assert palindrome("kajak") is True
    assert palindrome("Kajak") is True
    assert palindrome("A to idiota") is True
    assert palindrome("Ada, gwóźdź ów gada.") is True
