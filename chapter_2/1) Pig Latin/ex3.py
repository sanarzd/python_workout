def pig_latin_with_punctuation(word):
    punctuation = ''
    while word and not word[-1].isalpha():
        punctuation = word[-1] + punctuation
        word = word[:-1]
    if word[0].lower() in 'aeiou':
        result = f'{word}way'
    else:
        result = f'{word[1:]}{word[0]}ay'
    
    return result + punctuation


print(pig_latin_with_punctuation('python.'))   
print(pig_latin_with_punctuation('hello!'))    