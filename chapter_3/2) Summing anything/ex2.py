def mysum_bigger_than(threshold, *items):
    output = None

    for item in items:
        if item > threshold:
            if output is None:
                output = item
            else:
                output += item

    return output

print(mysum_bigger_than(10, 5, 20, 30, 6))