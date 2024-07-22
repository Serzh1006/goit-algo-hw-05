import timeit

mysetup = """
from __main__ import compute_lps
from __main__ import kmp_search
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


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


pattern = {
    't_word':"алгоритм",
    'new_word':"ноутбук"
}

raw = read_file("text_1.txt")
raw_1 = read_file("text_2.txt")

time_kmp_search_1 = timeit.timeit(stmt="kmp_search(raw, pattern['t_word'])", setup=mysetup, number=10)
time_kmp_search_2 = timeit.timeit(stmt="kmp_search(raw, pattern['new_word'])", setup=mysetup, number=10)
time_kmp_search_3 = timeit.timeit(stmt="kmp_search(raw_1, pattern['t_word'])", setup=mysetup, number=10)
time_kmp_search_4 = timeit.timeit(stmt="kmp_search(raw_1, pattern['new_word'])", setup=mysetup, number=10)

print(f"\ntime_kmp_search_1 = {time_kmp_search_1:.07f} seconds")
print(f"\ntime_kmp_search_2 = {time_kmp_search_2:.07f} seconds")
print(f"\ntime_kmp_search_3 = {time_kmp_search_3:.07f} seconds")
print(f"\ntime_kmp_search_4 = {time_kmp_search_4:.07f} seconds")