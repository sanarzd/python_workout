TEMPS = {
    '2026-06-01': 28,
    '2026-06-02': 30,
    '2026-06-03': 27,
    '2026-06-04': 29,
    '2026-06-05': 31,
    '2026-06-06': 26,
    '2026-06-07': 25,
}

def weather_lookup():
    date = input('Enter a date (YYYY-MM-DD): ').strip()

    if date in TEMPS:
        print(f'Temperature on {date}: {TEMPS[date]}')
    else:
        print('Date not found')

weather_lookup()