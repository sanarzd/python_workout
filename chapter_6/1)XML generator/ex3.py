def factorial(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


print(factorial(2, 3, 4))
print(factorial(5, 6))