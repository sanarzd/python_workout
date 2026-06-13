from pathlib import Path

def users_by_shell(filename):
    shells = {}

    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            fields = line.split(':')
            if len(fields) < 2:
                continue
            username = fields[0]
            shell = fields[-1]
            shells.setdefault(shell, []).append(username)
    return shells


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'sample.txt'
result = users_by_shell(file_path)
print(result)