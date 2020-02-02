"""
Napisz funkcję, która dla zadanej liczby zwróci parę liczb -
o jeden mniejsza i większą

nazwij funkcję up_down

up_down(5) -> (4,6)

"""
def up_down(number):
    return number - 1, number + 1

def test_up_down():
    assert up_down(5) == (4, 6)