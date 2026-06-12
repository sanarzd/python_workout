from pathlib import Path

def sum_products(filename):
    total = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue
            try:
                total += float(parts[0]) * float(parts[1])
            except ValueError:
                continue
    return total

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

print("Sum of products:", sum_products(file_path))