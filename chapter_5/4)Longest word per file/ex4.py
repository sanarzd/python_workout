from pathlib import Path
from collections import Counter

base_dir = Path(__file__).resolve().parent
log_path = base_dir / 'server.log'
status_counter = Counter()
with open(log_path, 'r') as f:
    for line in f:
        parts = line.split()
        for part in parts:
            if part.isdigit():
                status_counter[part] += 1
                break

for code, count in sorted(status_counter.items()):
    print(code, count)