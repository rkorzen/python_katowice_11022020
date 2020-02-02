"""
Napisz funkcję double_letters

która będzie analizować napis i sprawdzać czy zawiera powtarzające się obok siebie litery.
Jeśli tak zwraca True, w przeciwnym wypadku False

double_letters('ala') -> False
double_letters('alla') - > True
double_letters('nono') -> False
"""
def double_letters(text):
    for i in range(len(text)-1):
        if text[i] == text[i+1] and text[i].isalnum():
            return True
    return False

def test_double_letters():
    assert double_letters('ala') == False
    assert double_letters('alla') == True
    assert double_letters('al  la') == False
