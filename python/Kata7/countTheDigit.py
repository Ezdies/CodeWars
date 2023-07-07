def square_n(n):
    return [x * x for x in range(0, n + 1)]

def count_d(n, d):
    counter = 0
    while n > 0:
        if n % 10 == d:
            counter += 1
        n //= 10
    return counter

def nb_dig(n, d):
    squares = square_n(n)
    res = sum(map(lambda x: count_d(x, d), squares))
    if d == 0:
        res += 1
    return res


print(nb_dig(25, 1))