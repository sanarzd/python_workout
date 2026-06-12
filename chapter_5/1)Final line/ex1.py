from pathlib import Path

def get_final_line(filename):
    final_line = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            final_line = line
    return final_line

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

print("Final line:")
print(get_final_line(file_path), end='')


