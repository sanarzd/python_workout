from pathlib import Path

def find_404_errors(logfile):
    with open(logfile, 'r') as f:
        for line in f:
            if ' 404 ' in line:
                ip_address = line.split()[0]
                print(f"404 Error from IP: {ip_address}")


base_dir = Path(__file__).resolve().parent
log_file = base_dir / 'access.log'
find_404_errors(log_file)