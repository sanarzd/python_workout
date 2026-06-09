def dict_partition(d, f):
    true_dict = {}
    false_dict = {}

    for key, value in d.items():
        if f(key, value):
            true_dict[key] = value
        else:
            false_dict[key] = value

    return true_dict, false_dict


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def is_even(key, value):
    return value % 2 == 0

print(dict_partition(d, is_even))
