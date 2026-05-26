def truncate_float(number, before_digits, after_digits):
    str_number = str(number)
    
    if '.' in str_number:
        before_part, after_part = str_number.split('.')
    else:
        before_part = str_number
        after_part = ''
    truncated_before = before_part[-before_digits:] if len(before_part) >= before_digits else before_part
    
    truncated_after = after_part[:after_digits]
    
    result = float(truncated_before + '.' + truncated_after)
    return result


print(truncate_float(1234.5678, 2, 3))
