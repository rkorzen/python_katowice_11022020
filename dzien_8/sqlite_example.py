import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_pracownicy_table = """
CREATE TABLE IF NOT EXISTS pracownicy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  imie TEXT NOT NULL,
  nazwisko TEXT NOT NULL,
  rok_ur INTEGER,
  pensja REAL
);
"""


def create_pracownik_sql(pracownik):
    return """
INSERT INTO
  pracownicy (imie, nazwisko, rok_ur, pensja)
VALUES
  ('{}','{}',{},{});
""".format(*pracownik)


create_pracownicy = """
INSERT INTO
  pracownicy (imie, nazwisko, rok_ur, pensja)
VALUES
  ('James', "Dean", 1972, 60000),
  ('Ala', "Dean", 1974, 70000);
"""

select_pracownicy = "SELECT * from pracownicy"
if __name__ == "__main__":
    connection = create_connection("pracownicy.sqlite")
    execute_query(connection, create_pracownicy_table)
    execute_query(connection, create_pracownicy)
    pracownicy = execute_read_query(connection, select_pracownicy)

    print(pracownicy)
