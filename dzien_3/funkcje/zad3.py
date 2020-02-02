statuses = {
    "Alice": "online",
    "Rafał": "offline",
    "Anna": "online"
}

"""Napisz funkcję która przyjmie jako argument
słownik ze statusami, oraz status (napis)
I zwróci liczbę użytkowników o zadanym statusie
"""
def status_count(statuses, status):
    # counter = 0
    # for osoba, stat in statuses.items():
    #     if stat == status:
    #         counter += 1
    # return counter
    return list(statuses.values()).count(status)



def test_status_count():
    statuses = {
        "Alice": "online",
        "Rafał": "offline",
        "Anna": "online"
    }
    assert status_count(statuses, "online") == 2
    assert status_count(statuses, "offline") == 1
    assert status_count(statuses, "xxx") == 0
    assert status_count(None, "xxx") == 0

