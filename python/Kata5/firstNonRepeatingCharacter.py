def first_non_repeating_letter(s: str):
    
    if len(s) == 0:
        return ''
    occur = {char.lower(): s.lower().count(char.lower()) for char in s}

    for letter in s:
        if occur[letter.lower()] == 1:
            return letter
    return ''

print(first_non_repeating_letter('sTreSS'))