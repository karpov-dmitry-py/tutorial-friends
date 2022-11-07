friends = {
    'Jack': 'London',
    'Bill': 'Paris',
    'John': 'Rome',
}


def check_location(_friends, city):
    for friend, loc in _friends.items():
        if loc == city:
            result = f'{friend} живет в {loc}!'
        else:
            result = f'В {loc} у меня есть друг, но мне туда не нужно'

        print(result)


check_location(friends, 'Paris')
check_location(friends, 'NYC')
