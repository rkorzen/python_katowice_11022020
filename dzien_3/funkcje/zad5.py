"""
Napisz funkcję o nazwie: only_ints
która przyjmie 2 argumenty a i b
i zwróci True jeśli oba sa intami
w przeciwnym razie zwróci False

only_ints(1, 2) == True
only_ints("a", 1) == False
only_ints(1, True) == ??? False

"""

def only_ints(a, b):
    return type(a) == int and type(b) == int


def test_only_ints():
    assert only_ints(1, 2) == True
    assert only_ints(10, 20) == True
    assert only_ints("10", 20) == False
    assert only_ints("a", "b") == False
    assert only_ints(10, False) == False
