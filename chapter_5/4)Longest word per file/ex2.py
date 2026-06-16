from pathlib import Path
import hashlib

base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

def md5_of_file(filename):
    with open(filename, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

md5_hash = md5_of_file(file_path)
print(f'MD5: {md5_hash}')

