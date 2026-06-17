import csv
from pathlib import Path

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

base_dir = Path(__file__).resolve().parent
passwd_file = base_dir / 'my_passwd.txt'
output_file = base_dir / 'output.csv'

passwd_to_csv(passwd_file, output_file)