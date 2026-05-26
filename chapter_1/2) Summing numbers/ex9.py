def sum_numbers(items):
    total = 0
    for item in items:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            if item.lstrip("-").isdigit():
                total += int(item)
    return total

print(sum_numbers([1, "2", "hello", "10", "7"]))