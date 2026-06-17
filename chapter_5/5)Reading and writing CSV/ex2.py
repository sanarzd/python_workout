import csv
from pathlib import Path

fields_input = input("Enter space-separated field indices: ")
field_indices = [int(x) for x in fields_input.split()]
delimiter = input("Enter delimiter character: ")

base_dir = Path(__file__).resolve().parent
passwd_file = base_dir / 'my_passwd.txt'
output_file = base_dir / 'output.csv'

with open(passwd_file) as passwd, open(output_file, 'w') as out:
    reader = csv.reader(passwd, delimiter=':')
    writer = csv.writer(out, delimiter=delimiter)
    for record in reader:
        if len(record) > 1:
            selected = [record[i] for i in field_indices if i < len(record)]
            writer.writerow(selected)