from pathlib import Path

def letter_frequency(file_path):
    letter_counts = {}
    for one_line in open(file_path):
        for ch in one_line.lower():
            if ch.isalpha():
                letter_counts[ch] = letter_counts.get(ch, 0) + 1
    return letter_counts


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
freqs = letter_frequency(file_path)
sorted_items = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
top_five = sorted_items[:5]
print("Five most common letters:")
for letter, count in top_five:
    print(f"'{letter}': {count} times")