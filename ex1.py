import random
ex1_path = 'exercise/ex1.enc'
with open(ex1_path, 'r') as file:
    data = file.read().replace('\n', '')

cipher: str = "beijklmprsuvwyz"
real = "cdfgjklmnpqvwxz"

# custom mappings
mappings = [['f', 'h'], ['c', 'i'], ['h', 'b'], ['g', 'e'], ['n', 'a'], ['d', 't'], ['t', 's'], ['q', 'y'], ['a', 'u'],
            ['x', 'r'], ['r', 'v'], ['s', 'n'], ['z', 'g'], ['k', 'c'], ['b', 'l'], ['i', 'f'], ['j', 'd'], ['l', 'm']]

# frequency obtainer
frequencies = [0] * 26

data_alphachar_count = 0
for c in data:
    if (ord(c) - 97) > -1 < 26:
        data_alphachar_count += 1
        frequencies[ord(c) - 97] = frequencies[ord(c) - 97] + 1

alphabet = "abcdefghijklmnopqrstuvwxyz"
i: int
for i in range(26):
    print(alphabet[i], frequencies[i], str(int(100 * frequencies[i] / data_alphachar_count)) + "%")
print()

# building results string
results = ""
for c in data:
    found = False
    for m in mappings:
        if m[0] == c:
            results = results +  m[1]
            found = True
            break
    if not found:
        results = results + c
print(results)