from decimal import Decimal

def decimal_sum():
    first_input = input('Enter first number: ')
    second_input = input('Enter second number: ')
    first_decimal = Decimal(first_input)
    second_decimal = Decimal(second_input)
    sum_result = first_decimal + second_decimal
    print(f'{first_input} + {second_input} = {sum_result}')


decimal_sum()