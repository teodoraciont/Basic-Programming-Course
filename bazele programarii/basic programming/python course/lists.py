# example of list
neighborhoods_from_cluj = [
    'Manastur',
    'Ghiorgheni',
    'Grigorescu',
    'Marasti',
    'Buna Ziua',
    'Intre Lacuri',
    'Someseni',
    "Europa",
    "Bulgaria",
    "Borhanci"
]


def my_neighborhood():
    # access an element from a list
    return neighborhoods_from_cluj[0]


def your_neighborhood(position):
    # access an element from a list with a dynamic position
    return neighborhoods_from_cluj[position]


def get_multiple_words_neighborhood():
    """
    with append you can add an element to a list
    """
    result = []
    for neighborhood in neighborhoods_from_cluj:
        if ' ' in neighborhood:
            result.append(neighborhood)
    return result


def print_neighborhood_list(neighborhood_list):
    print_message_by_neighborhood_type(neighborhood_list)
    for neighborhood in neighborhood_list:
        print(neighborhood)


def print_message_by_neighborhood_type(neighborhood_list):
    if len(neighborhood_list) != len(neighborhoods_from_cluj):
        print("The neighborhood with 2 words are...")
    else:
        print("The neighborhood list is...")


def present_myself():
    print('Hi this is Theo, and I live in {} neighborhood'.format(my_neighborhood()))


def print_separator():
    print("********************************")


def insert_neighborhood_to_specific_index(index, neighborhood):
    print("Add {} in list at the position {}...".format(neighborhood, index))
    neighborhoods_from_cluj.insert(index, neighborhood)


def delete_from_specific_index(neighborhood):
    print("Remove {} from the list...".format(neighborhood))
    # if the doesn't exist in the list the code will return an error
    neighborhoods_from_cluj.remove(neighborhood)


if __name__ == '__main__':
    present_myself()
    print_separator()

    print_neighborhood_list(neighborhoods_from_cluj)
    print_separator()

    print_neighborhood_list(get_multiple_words_neighborhood())
    print_separator()

    insert_neighborhood_to_specific_index(4, 'Andrei Mureșanu')
    print_neighborhood_list(neighborhoods_from_cluj)
    print_separator()
    print_neighborhood_list(get_multiple_words_neighborhood())
    print_separator()

    delete_from_specific_index("Marasti")
    print_neighborhood_list(neighborhoods_from_cluj)
    print_separator()
    print_neighborhood_list(get_multiple_words_neighborhood())
    print_separator()
