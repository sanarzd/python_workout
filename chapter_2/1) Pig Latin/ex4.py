def pig_latin_advanced(word):
    vowels = set(c for c in word.lower() if c in 'aeiou')
    if len(vowels) > 1:
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


print(pig_latin_advanced('hello'))      
