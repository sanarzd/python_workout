def dict_merge(*dicts):
    output = {}
    for d in dicts:
        output.update(d)
    return output


print(dict_merge({'a': 1}, {'b': 2}, {'a': 3}))
