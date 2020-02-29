"""Zadanie domowe:
Dalekopis znaleziony w Saragossie
=================================
Grupa Twoich przyjaciół zajmujących się archelogią odnalazła w jednym z podziemnych bunkrów dziwną maszynę.
Ustalono, że jest to dalekopis.
Przy dalekopisie znaleziono taśmę, która miała w sobie dziurki.
Po dłuższym badaniu taśmy udało się ustalić, że dziurki i puste miejsca pogrupowane są w partie - po pięć.
Z uszkodzonej taśmy udało się odczytać następujące układy dziurek
    11111 10111 00111 00110 01110 01111 00100 11001 01010 11000 10011 01100 00100 01101 11000 11101 00100 01011 00111 11100 10110 00101 00100 11000 11110 00001 01010 00100 10000 10100 00001 00100 10010 00011 10001 10101 00100 01001 11000 11010 00100 00011 10010 10000 00001 01010 01100 00011 10000 00110 11110 00001 00100 00111 01110 10001 01110 00110 00001 00100 00101 00110 00001 00100 10110 10101 10000 10100 11000 01100 00011 00100 01111 10000 11000 00100 10001 01010 11000 11001 00110 10010 00100 01100 00110 00001 01110 10100 00100 10001 00011 10110 10101 10000 00011 00100 11000 00100 01100 00011 11010 01010 11000 01001 00001
1 - oznacza dziurkę
0 - brak dziurki.
Twoi przyjaciele nie wiedzą co z tym dalej zrobić, ale przypomnieli sobie, że jesteś na bootcampie z Pythona, a to wygląda na jakieś programistyczne zadanie.
"""
import pytest

figures = {'00000': 'NUL',
           '00001': '3',
           '00010': '\n',
           '00011': '-',
           '00100': ' ',
           '00101': '`',
           '00110': '8',
           '00111': '7',
           '01000': '\r',
           '01001': '\a',
           '01010': '4',
           '01011': 'Bell',
           '01100': ',',
           '01101': '!',
           '01110': ':',
           '01111': '(',
           '10000': '5',
           '10001': '+',
           '10010': ')',
           '10011': '2',
           '10100': '$',
           '10101': '6',
           '10110': '0',
           '10111': '1',
           '11000': '9',
           '11001': '?',
           '11010': '&',
           '11011': 'Figures',
           '11100': '.',
           '11101': '/',
           '11110': ';',
           '11111': 'Letters',
           }
letters = {'00000': 'NUL',
           '00001': 'E',
           '00010': '\n',
           '00011': 'A',
           '00100': ' ',
           '00101': 'S',
           '00110': 'I',
           '00111': 'U',
           '01000': '\r',
           '01001': 'D',
           '01010': 'R',
           '01011': 'J',
           '01100': 'N',
           '01101': 'F',
           '01110': 'C',
           '01111': 'K',
           '10000': 'T',
           '10001': 'Z',
           '10010': 'L',
           '10011': 'W',
           '10100': 'H',
           '10101': 'Y',
           '10110': 'P',
           '10111': 'Q',
           '11000': 'O',
           '11001': 'B',
           '11010': 'G',
           '11011': 'Figures',
           '11100': 'M',
           '11101': 'X',
           '11110': 'V',
           '11111': 'Letters',
           }

def decode(code, letters, figures):
    codes = code.split()
    source = "letters"
    napis = ''

    for element in codes:
        if letters[element] == 'Letters':  # '11111'
            source = "letters"
        elif letters[element] == 'Figures':
            source = "figures"
        else:
            # if source == 'letters':
            #     napis += letters[element]
            # elif source == 'figures':
            #     napis += figures[element]
            napis += globals().get(source)[element]
    return napis


def encode(inscription, letters, figures):
    result = []
    new_letters = {v: k for k, v in letters.items()}
    new_figures = {v: k for k, v in figures.items()}
    swich = ""

    for el in inscription:
        if el in new_letters:
            if swich != "new_letters":
                result.append(new_letters['Letters'])
                swich = "new_letters"
            result.append(new_letters[el])
        elif el in new_figures:
            if swich != "new_figures":
                result.append(new_figures['Figures'])
                swich = "new_figures"
            result.append(new_figures[el])
        else:
            raise ValueError(f"Znaku {el} nie da się zaszyfrować. Wybierz inny napis ")

    return " ".join(result)


def test_decode():
    assert decode("11111 10111 00111 00110 01110 01111", letters, figures) == "QUICK"


def test_encode():
    assert encode("QUICK", letters, figures) == "11111 10111 00111 00110 01110 01111"
    assert encode("QUICK1", letters, figures) == "11111 10111 00111 00110 01110 01111 11011 10111"
    with pytest.raises(ValueError):
        encode("QUIC@K", letters, figures)


code = "11111 10111 00111 00110 01110 01111 00100 11001 01010 11000 10011 01100 00100 01101 11000 11101 00100 01011 00111 11100 10110 00101 00100 11000 11110 00001 01010 00100 10000 10100 00001 00100 10010 00011 10001 10101 00100 01001 11000 11010 00100 00011 10010 10000 00001 01010 01100 00011 10000 00110 11110 00001 00100 00111 01110 10001 01110 00110 00001 00100 00101 00110 00001 00100 10110 10101 10000 10100 11000 01100 00011 00100 01111 10000 11000 00100 10001 01010 11000 11001 00110 10010 00100 01100 00110 00001 01110 10100 00100 10001 00011 10110 10101 10000 00011 00100 11000 00100 01100 00011 11010 01010 11000 01001 00001"


print(decode(code, letters,figures))
code = "ZGLASZAM SIE PO NAGRODE!"
print(encode(code, letters,figures))