# Dictionaries cannot have two items with the same key

old_phones = [
    {
        "name": "Sonny Ericsson",
        "model": "K750i",
        "color": "grey"
    },
    {
        "name": "Nokia",
        "model": "3310",
        "color": "blue"
    },
    {
        "name": "Huawei",
        "model": "BlackBerry Bold 9700",
        "color": "white"
    },
    {
        "name": "Samsung",
        "model": "Galaxy J5",
        "color": "black"
    },
    {
        "name": "Xiaomi",
        "model": "Mi A2",
        "color": "green"
    },
    {
        "name": "HTC",
        "model": "Desire 320",
        "color": "black"
    }
]


def get_favorite_phone_name():
    # search for an element
    for phone in old_phones:
        if phone['name'] == 'HTC':
            return phone["name"]


def get_ugglyest_phone():
    # search for an element
    for phone in old_phones:
        if phone['name'] == 'Sonny Ericsson':
            return phone


def put_a_ugly_mark():
    for phone in old_phones:
        if phone['name'] == 'Sonny Ericsson':
            phone['ugly'] = 'true'
            return phone


def get_ugglyest_phone_by_marker():
    for phone in old_phones:
        if phone.get("ugly", "") != "":
            return phone


if __name__ == '__main__':
    print('The list is... {}'.format(old_phones))
    print('My favorite phone is: {}'.format(get_favorite_phone_name()))
    # access a propriety
    print('The most ugglyest phone name was: {}'.format(get_ugglyest_phone()['name']))
    print('The most ugglyest phone model was: {}'.format(get_ugglyest_phone().get('model')))
    put_a_ugly_mark()
    print('The updated list is... {}'.format(old_phones))
    print('The most ugglyest phone by marker was: {}'.format(get_ugglyest_phone_by_marker()['name']))
