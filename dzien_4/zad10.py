"""
Napisz funkcję, która jako argument przyjmie listę list
i zwróci listę będącą ich połączeniem

flatten([[1, 2], [3, 4]]   ->  [1,2,3,4]

dodatkowo - sprbój napisać funkcję, która może przyjąć wiele argumentów, które sa listami
i zwróci ich połączenie

flatten([1,2], [3, 4], [4,5], ...) -> [1,2,3,4, 4, 5, ...]

"""


def flatten(*elements):  # *args
    if len(elements) == 1:
        elements = elements[0]
    result = []
    for el in elements:
        result.extend(el)
    return result


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([1, 2], [3, 4]) == [1, 2, 3, 4]
