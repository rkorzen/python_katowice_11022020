"""
Napisz 2 funkcje

add_dots
remove_dots

przyjmą one napis jako parametr
Pierwsza z nich ma wstawiać kropki pomiedzy znaki, np
add_dots('text') -> t.e.x.t

druga odwrotnie:
remove_dots('t.e.x.t') -> text

"""


def add_dots(param):
    # rezult=""
    # last_index = len(param) - 1
    # for i, l in enumerate(param):
    #     rezult += l
    #     if i < last_index:
    #         rezult += "."
    # return rezult
    return ".".join(param)

def test_add_dots():
    assert add_dots("text") == "t.e.x.t"


def remove_dots(param):
    # return "".join(param.split("."))
    return param.replace(".","")


def test_remove_dots():
    assert remove_dots("t.e.x.t") == 'text'

