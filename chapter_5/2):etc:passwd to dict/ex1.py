from pathlib import Path

def passwd_to_dict(filename):
    users = {}

    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            line = line.strip()

            if not line or line.startswith('#'):
                continue

            fields = line.split(':')

            if len(fields) < 3:
                continue

            users[fields[0]] = int(fields[2])

    return users


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'

users = passwd_to_dict(file_path)
print(users)