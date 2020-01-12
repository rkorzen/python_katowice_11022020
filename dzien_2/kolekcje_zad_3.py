lista = [10, -1, 20, -100, 3]

ld = 0
lu = 0

for l in lista:
    if l < 0:
        lu += 1
    else:
        ld += 1

print("""
liczb dodatnich: {}
liczb ujemnych: {}
""".format(ld, lu))

print(f"""
liczb dodatnich: {ld}
liczb ujemnych: {lu}
""")

print("""
liczb dodatnich: %s
liczb ujemnych: %s
""" % (ld, lu))

print("""
liczb dodatnich: """ + str(ld) + """
liczb ujemnych: """ + str(lu) )