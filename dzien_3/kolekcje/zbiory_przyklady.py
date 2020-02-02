print(set)
print(set())

print(set([1, 2, 3]))

print(set([1, 1, 1, 2, 3, "a"]))

x = set("abcabc")
x.add('d')
for i in x:
    print(i)

print(dir(x))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)
print(A - B)
print(A & B)
print(A ^ B)
