from collections import Counter

def show_shells_by_popularity():
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
    counts = Counter(shells)
    for shell, count in counts.most_common():
        print(shell, count)

show_shells_by_popularity()