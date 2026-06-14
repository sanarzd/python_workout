from pathlib import Path
import os

def get_file_size(file_path):
    return os.stat(file_path).st_size


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
size = get_file_size(file_path)
print(f"sample.txt size: {size} bytes")