def anyjoin(sequence, glue=' '):
    return glue.join(str(item) for item in sequence)

print(anyjoin([1, 2, 3]))
print(anyjoin("abc", "**"))