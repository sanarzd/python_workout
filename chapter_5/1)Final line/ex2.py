from pathlib import Path

def sum_numbers_in_file(filename):
    total = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                try:
                    total += int(word)
                except ValueError:
                    pass
    return total

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

print("Sum of numbers:", sum_numbers_in_file(file_path))