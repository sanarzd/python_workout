words = ["apple", "Banana", "CHERRY", "date", "fig"]

def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

sorted_words = sorted(words, key=count_vowels)
print(sorted_words)