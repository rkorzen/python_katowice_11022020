import re

with open("input.txt") as f:
    text = f.read()

email_pattern = re.compile("([\w-]+@\w+(?:\.\w+)+)")
pna_pattern = re.compile("\d{2}-\d{3}")
data_pattern = re.compile("\d{2} \w{3} \d{4}")

print("emaile", email_pattern.findall(text))
print("kody", pna_pattern.findall(text))
print("daty", data_pattern.findall(text))

