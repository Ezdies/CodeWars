def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        years += 1
        principal += principal * interest * (1 - tax)
    return years

print(calculate_years(1000, 0.05, 0.18, 1100))