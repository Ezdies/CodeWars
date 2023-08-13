import math

def isPP(n):
    max_exponent = int(math.log(n, 2)) + 1
    for base in range(2, int(math.sqrt(n)) + 1):
        exponent = 2
        while base ** exponent <= n and exponent <= max_exponent:
            if base ** exponent == n:
                return [base, exponent]
            exponent += 1
    return None

            
        
        