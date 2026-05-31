def even_odd_sums(numbers):
    return [sum(numbers[::2]), sum(numbers[1::2])]

print(even_odd_sums([10, 20, 30, 40, 50, 60]))  
