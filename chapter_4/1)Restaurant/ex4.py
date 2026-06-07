from datetime import date

FAMILY = {
    'maria': date(1995, 4, 10),
    'ali': date(1990, 9, 23),
    'sara': date(2001, 1, 5),
}

def age_in_days():
    name = input('Enter a family member name: ').strip().lower()

    if name in FAMILY:
        today = date.today()
        age_days = (today - FAMILY[name]).days
        print(f'{name} is {age_days} days old')
    else:
        print('Name not found')

age_in_days()