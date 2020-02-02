
def kwadraty(n):
    wynik = [i**2 for i in range(n)]
    return wynik


def hello():
    print("Hello")

def sumuj(a, b):
    print(a, b)
    return a + b

n2 = kwadraty(2)
n3 = kwadraty(3)
n10 = kwadraty(10)

print(n2)
print(n3)
print(n10)

h = hello()
print(h)
# suma = sumuj(10, 20, 30)
# print(suma)


### zasięgi

a = 1
print(locals())
print(globals())
print('-'*40)
def incr_a():
    #global a
    a = 10
    print(locals())
    print(globals())
    print("w", a)

incr_a()
print("a", a)
