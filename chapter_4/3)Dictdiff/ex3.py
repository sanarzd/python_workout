def make_dict(*args):
    if len(args) % 2 != 0:
        raise ValueError("Number of arguments must be even")

    output = {}
    for i in range(0, len(args), 2):
        output[args[i]] = args[i + 1]
    return output


print(make_dict('a', 1, 'b', 2))
