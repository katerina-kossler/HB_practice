def add_new_rating():
    """Restaurant rating adder.
    """

    new_restaurant_name = input("What restaurant would you like to add to the"
                                " rating database? > ")
    new_restaurant_name = new_restaurant_name.title()

    while True:
        new_restaurant_rating = input("How would you rate this? (1-5) > ")
        if new_restaurant_rating.isdigit():
            break

    return new_restaurant_name, new_restaurant_rating


def restaurant_rater(raw_ratings):
    """Restaurant rating lister.
    Store restaurant data and ratings in dictionary.
    Print ratings alphabetically by restaurant.
    """

    restaurant_dict = {}

    restaurant_file = open(raw_ratings)
    for line in restaurant_file:
        line = line.rstrip()
        restaurant_info = line.split(':')
        restaurant_name, restaurant_rating = restaurant_info
        restaurant_dict[restaurant_name] = restaurant_rating

    new_restaurant_name, new_restaurant_rating = add_new_rating()

    if new_restaurant_name not in restaurant_dict:
        restaurant_dict[new_restaurant_name] = new_restaurant_rating

    sorted_names = sorted(restaurant_dict)

    for name in sorted_names:
        print("{} is rated at {}.".format(name, restaurant_dict[name]))

    # restaurant_list = restaurant_dict.items()
    # restaurant_list = sorted(restaurant_list)
    # restaurant_list.sort()
    # for name, rating in restaurant_list:
    #     print("{} is rated at {}.".format(name, rating))


restaurant_rater("scores.txt")
