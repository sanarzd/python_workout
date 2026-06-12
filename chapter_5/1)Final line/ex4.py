from pathlib import Path

def count_vowels(filename):
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for char in line.lower():
                if char in vowels:
                    vowels[char] += 1
    return vowels

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

counts = count_vowels(file_path)
print(counts)