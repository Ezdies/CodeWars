def cakes(recipe, available):
    max_cakes = float('inf')  # Ustawiamy maksymalną ilość ciastek jako nieskończoność

    for ingredient, amount in recipe.items():
        if ingredient not in available or available[ingredient] < amount:
            return 0
        max_cakes = min(max_cakes, available[ingredient] // amount)

    return max_cakes
    
    
    
    