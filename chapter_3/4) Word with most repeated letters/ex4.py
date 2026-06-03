from collections import Counter, defaultdict

def show_shells_and_users():
    shell_to_users = defaultdict(list)
    shells = []
    with open('/etc/passwd') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            fields = line.split(':')
            username = fields[0]
            shell = fields[-1]
            shells.append(shell)
            shell_to_users[shell].append(username)
    counts = Counter(shells)
    for shell, count in counts.most_common():
        users = sorted(shell_to_users[shell])
        print(f'{shell} ({count}): {", ".join(users)}')

show_shells_and_users()