
# try:
#     fh = open('logs.txt')
#     print(dir(fh))
#     1/0
# finally:
#     print("To sie wykona zawsze")
#     fh.close()
#
# context manager;
# with open("logs.txt") as logi:
#     with open("emails.txt") as emaile:
#         print(emaile.read())
#     print(logi.read())

with open("test.txt", "w", encoding="utf8") as f:
    f.write("ala ma kota\n")
    f.write("kot ma Alę")
