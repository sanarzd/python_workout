from pathlib import Path

def passwd_to_nested_dict(filename):
    users = {}

    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            fields = line.split(':')
            if len(fields) < 4:
                continue
            username = fields[0]
            uid = int(fields[2])
            home_dir = fields[-2]
            shell = fields[-1]
            users[username] = {
                'uid': uid,
                'home_dir': home_dir,
                'shell': shell
            }
    return users


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
result = passwd_to_nested_dict(file_path)
print(result)