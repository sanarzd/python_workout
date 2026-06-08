from collections import defaultdict

def group_ips_by_status(log_filename):
    codes = defaultdict(list)

    with open(log_filename, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) < 1:
                continue

            status_code = parts[-2]
            ip = parts[0]
            codes[status_code].append(ip)

    for code, ips in codes.items():
        print(f'{code}: {ips}')