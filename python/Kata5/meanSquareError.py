def solution(array_a, array_b):
    return sum([pow(abs(a-b),2) for a, b in zip(array_a, array_b)]) / len(array_a)

print(solution([10, 20, 10, 2],[10, 25, 5, -2]))