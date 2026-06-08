def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name: ').strip()

        if not city_name:
            break

        mm_rain = int(input('Enter mm rain: ').strip())

        rainfall[city_name] = rainfall.get(city_name, 0) + mm_rain

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')