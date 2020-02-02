"""
mamy plansze do gry w kółko i krzyżyk

1:  X | O | X
   -----------
2:    |   |
   -----------
3:  O |   |
    A   B  C


board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

Napisz funkcję get_row_col

która przyjmie napis odpowiadajacy położeniu na planszy np.:

A1, C2 i zwróci koordynaty
get_row_col("A3") -> (2, 0)

"""


def get_row_col(position):
    columns = "ABC"
    rows = "123"
    col_n, row_n = list(position)
    try:
        return rows.index(row_n), columns.index(col_n)
    except ValueError:
        return "Koordynata spoza planszy"


def test_get_row_col():
    assert get_row_col("A3") == (2, 0)
    assert get_row_col("C3") == (2, 2)
    assert get_row_col("D3") == "Koordynata spoza planszy"
