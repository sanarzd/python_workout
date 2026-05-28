def pig_latin_capitalized(word):
    if word[0].lower() in 'aeiou':
        result = f'{word}way'
    else:
        result = f'{word[1:]}{word[0]}ay'
    if word[0].isupper():
        return result[0].upper() + result[1:].lower()
    return result.lower()


print(pig_latin_capitalized('Python'))    
