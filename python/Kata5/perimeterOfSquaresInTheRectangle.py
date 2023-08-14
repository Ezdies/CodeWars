def perimeter(n):
    tab = [1,1]
    [tab.append(tab[i] + tab[i-1]) for i in range(1, n)]
    return sum(tab) * 4

print(perimeter(5))
    