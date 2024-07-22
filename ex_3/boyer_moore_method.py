import timeit

mysetup = """
from __main__ import build_shift_table
from __main__ import boyer_moore_search
from __main__ import raw
from __main__ import raw_1
from __main__ import pattern
"""

def read_file(path):
    try:
        with open(path, 'r', encoding='cp1251') as file:
            return file.read()
    except UnicodeDecodeError as e:
        print(f"{e}")


def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

pattern = {
    't_word':"алгоритм",
    'new_word':"ноутбук"
}

raw = read_file("text_1.txt")
raw_1 = read_file("text_2.txt")

time_boyer_moore_1 = timeit.timeit(stmt="boyer_moore_search(raw, pattern['t_word'])", setup=mysetup, number=10)
time_boyer_moore_2 = timeit.timeit(stmt="boyer_moore_search(raw, pattern['new_word'])", setup=mysetup, number=10)
time_boyer_moore_3 = timeit.timeit(stmt="boyer_moore_search(raw_1, pattern['t_word'])", setup=mysetup, number=10)
time_boyer_moore_4 = timeit.timeit(stmt="boyer_moore_search(raw_1, pattern['new_word'])", setup=mysetup, number=10)

print(f"\ntime_boyer_moore_1 = {time_boyer_moore_1:.07f} seconds")
print(f"\ntime_boyer_moore_2 = {time_boyer_moore_2:.07f} seconds")
print(f"\ntime_boyer_moore_3 = {time_boyer_moore_3:.07f} seconds")
print(f"\ntime_boyer_moore_4 = {time_boyer_moore_4:.07f} seconds")