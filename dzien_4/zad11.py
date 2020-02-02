"""

Napisz funkcję  largest_difference, która przyjmie listę elementów
i zwróci największa różnicę miedzy nimi

largest_differrence([1,2,3,10]) == 9

napisz funkcję larges_difference2 która zadziala podobnie
ale argumenty podajemy osobno a nie w liscie

largest_differrence(1, 2, 3, 10) == 9

"""


def largest_difference(elements):
    if elements:
        return max(elements) - min(elements)


def largest_difference2(*elements):
    if elements:
        return max(elements) - min(elements)


def test_largest_difference():
    assert largest_difference([1, 2, 3, 10]) == 9
    assert largest_difference([]) is None
    assert largest_difference([1]) == 0


def test_largest_difference2():
    assert largest_difference2(1, 2, 3, 10) == 9
    assert largest_difference2() is None
    assert largest_difference2(1) == 0
