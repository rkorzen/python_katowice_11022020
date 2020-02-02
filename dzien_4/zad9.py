"""
Dwa napisy są anagramami jeśli można z liter jednego,
poprzez ich przestawienie zrobić drugi

Napisz funkcję:

is_anagram, która przyjmie dwa napisy i sprawdzi czy są anagramami

"""

a = "Tokio"  # noqa
b = "Bob"


# sprawdzanie typowania - adnotacje. Narzędzie np. mypy
# pip install flake8
def is_anagram(a: str, b: str) -> bool:
    """
    Sprawdza czy dwa napisy to anagramy

    :param a: str
    :param b: str
    :return: bool
    """
    return sorted(a.lower()) == sorted(b.lower())


def test_is_anagram():
    assert is_anagram('Tokio', 'Kioto') is True
    assert is_anagram("Anna", "Bob") is False
