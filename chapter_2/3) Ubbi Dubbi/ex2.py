def ubbi_dubbi(word):
    output = []
    for letter in word.lower():
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)

    result = ''.join(output)

    if word.istitle():
        result = result.capitalize()

    return result

print(ubbi_dubbi('elephant')) 