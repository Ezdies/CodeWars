def cut_the_ropes(arr):
    counter_arr = []
    while any(number > 0 for number in arr):
        mini = min(num for num in arr if num > 0)
        non_zero_count = sum(True for num in arr if num > 0 and num >= mini)
        arr = [num - mini for num in arr if num > 0]
        counter_arr.append(non_zero_count)
    return counter_arr


my_array = [3, 3, 2, 9, 7]
result = cut_the_ropes(my_array)
print(result)  # Output: [5, 4, 2, 1]

