#does not compile, just wanted to try this approach, it is not time optimalized
from itertools import permutations

def next_bigger(n):
    digits = [int(digit) for digit in str(n)]
    permutation_numbers = [int(''.join(map(str, perm))) for perm in permutations(digits)]
    permutation_numbers = sorted(list(set(permutation_numbers)))
    permutation_numbers = [number for number in permutation_numbers if number > n]
    
    return permutation_numbers[0] if permutation_numbers else -1

print(next_bigger(2017)) #2071