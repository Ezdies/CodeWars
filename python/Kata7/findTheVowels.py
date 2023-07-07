def is_vowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for x in vowels:
        if str.lower(c) == x:
            return True
    return False

def vowel_indices(word):
    indices = []
    for (i, c) in enumerate(word):
        if is_vowel(c):
            indices.append(i + 1)
    return indices

print(vowel_indices("Apple"))
        