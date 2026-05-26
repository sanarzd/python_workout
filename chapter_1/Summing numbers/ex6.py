def mysum(numbers, start = 0):
    output = start
    for number in numbers:
        output += number
    return output

print(mysum([10, 20, 30, 40]))
print(mysum([10, 20, 30, 40], 50))    