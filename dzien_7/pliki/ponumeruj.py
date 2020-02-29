import sys
if len(sys.argv) > 1:
    plik = sys.argv[1]
else:
    plik = "dane/emails.txt"

with open(plik) as f:
    for i, line in enumerate(f, start=1):
        print(i, line[:-1])
