from pathlib import Path

def get_unique_ips(file_path):
    unique_ips = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split()
            if parts:
                unique_ips.add(parts[0])

    return unique_ips


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.log'

ips = get_unique_ips(file_path)
print("Unique IPs:")
for ip in sorted(ips):
    print(ip)

print("Count:", len(ips))