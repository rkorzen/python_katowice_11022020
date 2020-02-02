"""
Napisz funkcję o nazwie: mid,
która przyjmie jako parametr napis.
Funkcja ma wybrać i zwrócić środkową literę
Jeśli środkowej litery nie ma, to pusty napis
Dopisz testy
mid("abc") -> 'b'
mid("aabbcc") -> ''

"""
def mid(text):
    if len(text) % 2 == 0:
        return ""
    return text[len(text)//2]

def test_mid_without_middle_letter():
    assert mid("aabbcc") == ""

def test_mid_with_middle_letter():
    assert mid("abc") == "b"
    assert mid("doremifasol") == "i"

def test_mid_empty_string():
    assert mid("") == ""

