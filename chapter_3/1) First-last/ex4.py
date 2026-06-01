def myzip(*iterables):
    result = []
    for items in zip(*iterables):
        result.append(items)
    return result


print(myzip([10, 20, 30], 'abc'))
