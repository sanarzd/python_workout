from pathlib import Path

def last_word_alphabetically(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
    return sorted(words)[-1]

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'text.txt'

print(last_word_alphabetically(file_path))