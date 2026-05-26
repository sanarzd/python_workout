def average(numbers):
    l = len(numbers)
    output = 0
    for number in numbers:
        output += number
    avg = output / l
    return avg

print(average([10, 20, 30, 40]))
    
'''
def average(numbers):
    return sum(numbers) / len(numbers)

print(average([10, 20, 30, 40]))

'''
    