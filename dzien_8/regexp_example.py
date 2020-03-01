import re

pattern = re.compile(" \w{8} ")
pattern2 = re.compile("\d\d\d-\d\d\d")
# with open("pan-tadeusz.txt", encoding="utf8") as text:
#     wyniki = pattern.findall(text.read())

# print(wyniki)
print(pattern2.match("123-123"))
pattern2.