import operator

MOVIES = [
    ('Oppenheimer', 180, 'Christopher Nolan'),
    ('Poor Things', 141, 'Yorgos Lanthimos'),
    ('Killers of the Flower Moon', 206, 'Martin Scorsese')
]

def sort_movies(list_of_tuples):
    choice = input('Sort by title, length, or director? ')

    field_map = {
        'title': 0,
        'length': 1,
        'director': 2
    }

    key_index = field_map[choice]

    output = []
    template = '{0:30} {1:5} {2:20}'

    for movie in sorted(list_of_tuples, key=operator.itemgetter(key_index)):
        output.append(template.format(*movie))

    return '\n'.join(output)

print(sort_movies(MOVIES))