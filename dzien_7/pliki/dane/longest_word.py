"""
$ longest_word.py text.txt
abrkabadabra

"""
import string

file_name = "pan-tadeusz.txt"

def clean(text):
    znaki = string.ascii_lowercase + "ąćęłóńśźż- "
    uniq_text = set(text)
    for znak in uniq_text:
        if znak not in znaki:
            text = text.replace(znak, "")
    return text

def prepare_text(file_name):
    with open(file_name, encoding="utf-8") as f:
        text = f.read().lower()
        for el in "\n\\:/":
            text = text.replace(el, " ")
        text = clean(text)
    return text.split()

def longest_words(file_name):
        text = prepare_text(file_name)
        text = set(text.split())
        dlugosci = {slowo: len(slowo) for slowo in text}

        print(sorted(dlugosci.items(), key=lambda x: x[1], reverse=True))
["ala", "ala", "bela"]
[("ala", 10), ("bela", 20)]

def most_frequent_words(file_name):
    text = prepare_text(file_name)
    frequencies = {word: text.count(word) for word in set(text) if len(word) > 3}
    return sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

print(most_frequent_words(file_name))


freq = {}

for word in set(text):
    if len(word) > 3:
        freq[word] = text.count(word)

# with open(file_name, encoding='utf8') as f:
#     text = f.read()
#     print(text.count('dżuma'))