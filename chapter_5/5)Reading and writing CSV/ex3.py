import csv

def dict_to_csv(d, filename):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for key, value in d.items():
            writer.writerow([key, value, type(value).__name__])

my_dict = {'name': 'Ali', 'age': 30, 'score': 95.5}
dict_to_csv(my_dict, 'dict_output.csv')

           