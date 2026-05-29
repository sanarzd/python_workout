from pathlib import Path

def nonsensical_sentence(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result = []
    for i, line in enumerate(lines[:10], start=1):
        words = line.split()
        if len(words) >= i:
            result.append(words[i - 1])

    print(' '.join(result))

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
nonsensical_sentence(file_path)