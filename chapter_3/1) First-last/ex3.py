def plus_minus(numbers):
    total = 0
    sign = 1
    for number in numbers:
        total += sign * number
        sign *= -1
    return total



print(plus_minus((1, 2, 3, 4))) 