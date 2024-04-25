def best_friend(txt, a, b):
    if txt.endswith(a):
        return False
    for i in range(len(txt) - 1):
        if txt[i] == a and txt[i + 1] != b:
            return False
    return True


