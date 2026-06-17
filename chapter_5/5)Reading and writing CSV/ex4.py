import csv
import random

with open('random.csv', 'w') as f:
    writer = csv.writer(f)
    for _ in range(5):  
        writer.writerow([random.randint(10, 100) for _ in range(10)])

with open('random.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        nums = [int(x) for x in row]
        print(sum(nums), sum(nums) / len(nums))