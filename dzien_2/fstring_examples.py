print(f"xxx {10} xxx")

print(f"xxx {10:8} xxx")
print(f"xxx {10:<8} xxx")
print(f"xxx {10:^8} xxx")
print(f"xxx {10:^8.2f} xxx")

print(f"xxx {100000000:,} xxx")

# https://realpython.com/python-f-strings/

## Wybrane operacje na stringach

# print(dir(""))

# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', \
# # 'isdigit', 'isidentifier', 'islower', 'isnumeric', \
# # 'isprintable', 'isspace', 'istitle', 'isupper', 'join',\
# # 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', \
# # 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',\
# # 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',\
# # 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

napis = "   ala MA KoTa  ;Kot ma ale ; ala "
print(napis)
print(napis.strip())
print(napis.lstrip())
print(napis.rstrip())
print(napis.lower())
print(napis.upper())
print(napis.title())
print(napis.strip().capitalize())
print(napis.lower().replace('ala', 'ola'))

log = """999|user login
1000|user logout"""

logs = log.splitlines()
print(logs)

for l in logs:
    print(l.split("|"))

for znak in log:
    print(znak)

print(log[:10])