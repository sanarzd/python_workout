def get_rainfall_with_average():
    rainfall = {}
    counts = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = int(input('Enter mm rain: '))
        rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain
        counts[city_name] = counts.get(city_name, 0) + 1

    for city in rainfall:
        total = rainfall[city]
        average = total / counts[city]
        print(f'{city}: total={total}, average={average:.2f}')


get_rainfall_with_average()