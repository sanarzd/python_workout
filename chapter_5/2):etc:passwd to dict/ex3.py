def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

def factors_dict(numbers):
    result = {}
    for number in numbers:
        for factor in factors(number):
            result.setdefault(factor, []).append(number)
    return result


user_input = input("Enter integers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
print(factors_dict(numbers))