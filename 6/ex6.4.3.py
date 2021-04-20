cities = {
    'shihezi': {
        'country': 'China',
        'population': 'jibaiwan',
        'fact':'huayuan',
        },
    'lundun': {
        'country': 'Kindom',
        'populaton': 'haojibaiwan',
        'fact': 'cengjia'
        },
    }
for city, city_info in cities.items():
    print("\n" + city.title() + ":")
    for info, rt in city_info.items():
        print("\t" + info + ":" + rt.title())