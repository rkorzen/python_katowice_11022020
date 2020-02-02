"""
Napisz funkcję, która zwróci długość najdłuższego ciągu
tego samego znaku w napisu

np:

consecutive("aabbbaabbbb", "b") -> 4
"""
import re

def consecutive(text, sign):
    longest_counter = 0
    counter = 0
    for s in text:
        if s == sign:
            counter += 1
        else:
            longest_counter = max(counter, longest_counter)
            counter = 0
    longest_counter = max(counter, longest_counter)
    return longest_counter


def consecutive(text, sign):
    pattern = re.compile(f"{sign}*")
    data = pattern.findall(text)
    # data = [len(x) for x in data]
    data = map(lambda x: len(x), data)
    return max(data)





def test_consecutive():
    assert consecutive("aabbbaabbbb", "b") == 4
    assert consecutive("aabbbaabbbb", "a") == 2
    assert consecutive("aabbbbaabbb", "b") == 4
