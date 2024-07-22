import timeit

mysetup = """
from __main__ import polynomial_hash
from __main__ import rabin_karp_search
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

def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256 
    modulus = 101  

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

pattern = {
    't_word':"алгоритм",
    'new_word':"ноутбук"
}

raw = read_file("text_1.txt")
raw_1 = read_file("text_2.txt")

time_rabin_karp_1 = timeit.timeit(stmt="rabin_karp_search(raw, pattern['t_word'])", setup=mysetup, number=10)
time_rabin_karp_2 = timeit.timeit(stmt="rabin_karp_search(raw, pattern['new_word'])", setup=mysetup, number=10)
time_rabin_karp_3 = timeit.timeit(stmt="rabin_karp_search(raw_1, pattern['t_word'])", setup=mysetup, number=10)
time_rabin_karp_4 = timeit.timeit(stmt="rabin_karp_search(raw_1, pattern['new_word'])", setup=mysetup, number=10)

print(f"\ntime_rabin_karp_1 = {time_rabin_karp_1:.07f} seconds")
print(f"\ntime_rabin_karp_2 = {time_rabin_karp_2:.07f} seconds")
print(f"\ntime_rabin_karp_3 = {time_rabin_karp_3:.07f} seconds")
print(f"\ntime_rabin_karp_4 = {time_rabin_karp_4:.07f} seconds")