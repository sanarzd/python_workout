def word_length(words):
    shortest = min(len(word) for word in words)
    longest = max(len(word) for word in words)
    average = sum(len(word) for word in words) / len(words)

    return (shortest, longest, average)



words = ["cat", "elephant", "dog", "butterfly"]
result = word_length(words)
print(f"result: {result}")
print(f"shortest: {result[0]}")
print(f"longest: {result[1]}")
print(f"average: {result[2]}")


