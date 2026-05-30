from pathlib import Path

def longest_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
    return sorted(words, key=len)[-1]

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'text.txt'

print(longest_word(file_path))