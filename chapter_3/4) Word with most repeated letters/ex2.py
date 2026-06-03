from collections import Counter

def most_repeating_vowel_count(word):
    vowels = 'aeiouAEIOU'
    filtered = [ch for ch in word if ch in vowels]
    if not filtered:
        return 0
    return Counter(filtered).most_common(1)[0][1]

def most_repeating_vowel_word(words):
    return max(words, key=most_repeating_vowel_count)

words = ['this', 'is', 'an', 'elementary', 'test', 'example']
print(most_repeating_vowel_word(words))