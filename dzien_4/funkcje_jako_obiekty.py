

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b:
        return a / b


def eval(string):  # "1 + 2"
    a, op, b = string.split()
    a, b = int(a), int(b)
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    operation = operations[op]
    return operation(a, b)

print(eval("123 / 124"))

x = print
x("To działą")

def drugi(x):
    return x[1]

lambda x: x[1]

lista = ["2g", "8a", "4c"]
print(sorted(lista, key=drugi))
print(sorted(lista, key=lambda x: x[1]))