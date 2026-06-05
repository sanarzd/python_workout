from collections import namedtuple
import operator

Person = namedtuple('Person', ['first', 'last', 'hours'])

PEOPLE = [
    Person('Donald', 'Trump', 7.85),
    Person('Vladimir', 'Putin', 3.626),
    Person('Jinping', 'Xi', 10.603)
]

def format_sort_records(list_of_people):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'

    for person in sorted(list_of_people, key=operator.attrgetter('last', 'first')):
        output.append(template.format(person.first, person.last, person.hours))

    return '\n'.join(output)

print(format_sort_records(PEOPLE))