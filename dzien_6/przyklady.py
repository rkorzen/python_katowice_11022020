import math

class Square:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"<Square a:{self.a:.2f}>"

    def __add__(self, other):
        if isinstance(other, Square):
            area = self.area + other.area
            a = math.sqrt(area)

        elif isinstance(other, int):
            a = self.a + other
        return Square(a)

    def __radd__(self, other):
        return self.__add__(other)

    # __sub__
    # __mul__
    # __
    @property
    def area(self):
        return self.a ** 2

s1 = Square(3)
s2 = Square(4)
print(s1)
print(s1 + s2)
print(s1 + 4)
print(4 + s1)
s1.__add__(s2)