import time


def zmierz_czas(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("Czas wykonania:", time.time() - start)
        return result

    return wrapper

@zmierz_czas
def sum_of_squares(n):
    return sum(i**2 for i in range(n))

@zmierz_czas
def sumator(*args):
    return sum(args)


# sum_of_squares = zmierz_czas(sum_of_squares)
# sumator = zmierz_czas(sumator)
print(sum_of_squares(100000))


class Zwierz:

    def __init__(self, gatunek, imie, waga_kg):
        self.gatunek = gatunek
        self.imie = imie
        self.waga_kg = waga_kg

    @property
    def waga_w_funtach(self):
        return self.waga_kg * 2.20462262


zwierz = Zwierz("xxx", "yyy", 10)
print(zwierz.waga_w_funtach)

zwierz.waga_w_funtach = 1000