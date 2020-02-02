import random
"""
Napisz funkcję, random_number,
która nie przyjmuje argumentów
a zwraca losową liczbę z przedziału 1-100 
"""

def random_number():
    return random.randint(1, 101)

print(random_number())

def test_random_number():
    random.seed(0)
    assert random_number() == 50
    random.seed(10)
    assert random_number() == 74