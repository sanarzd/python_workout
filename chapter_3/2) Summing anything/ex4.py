def combine_dicts(dicts):
    result = {}

    for d in dicts:
        for key, value in d.items():
            if key not in result:
                result[key] = [value]
            else:
                result[key].append(value)

    return result

print(combine_dicts([
    {'a': 1, 'b': 2},
    {'a': 3, 'c': 4},
    {'b': 5, 'd': 6}
]))