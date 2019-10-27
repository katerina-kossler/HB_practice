"""Restaurant rating lister."""


def restaurant_rater (filename):
    #open file with restaurant lists
    #create empty dictionary
    file = open(filename)
    restaurant_ratings = {}
    #loop though restaurant lists
    for line in file:
        line = line.rstrip()
        restaurants_info = line.split(":")
        restaurant_name = restaurants_info[0]
        rating = restaurants_info[1]

        #add to the dictionary
        restaurant_ratings[restaurant_name] = rating

    new_restaurant_name = input("What is the cool new restaurant you went to?")
    # take restaurant rating
    new_rating = input("What is your rating of this restaurant.")
    # store new rating in restaurante_ratings

    restaurant_ratings[new_restaurant_name] = new_rating

    # create new list of key-value tuples and sort list (asc), then unpacks the
    # name and rating for easy printing
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(restaurant + " is rated at " + rating + ".")




restaurant_rater('scores.txt')
