############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

    def __repr__(self):
        return self.name

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')  
    # instantiates muskmelon
        self.first_harvest = first_harvest
    muskmelon.add_pairing('mint') 
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')  
    # instantiates Casaba
    casaba.add_pairing('strawberries') 
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f" - {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dictionary = {}
    for melon in melon_types:
        melon_dictionary[melon.code] = melon

    return melon_dictionary
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, code, shape_rating, color_rating, field, harvestor):
        self.code = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvestor = harvestor

    def is_sellable(self):
        is_shapley = self.shape_rating > 5
        is_colorful = self.color_rating > 5
        not_poisonous = self.field != 3
        return is_shapley and is_colorful and not_poisonous
 

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_list = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_list.append(melon_1)
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Shelia')
    melon_list.append(melon_2)
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Shelia')
    melon_list.append(melon_3)
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Shelia')
    melon_list.append(melon_4)
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_list.append(melon_5)
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_list.append(melon_6)
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_list.append(melon_7)
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_list.append(melon_8)
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Michael')
    melon_list.append(melon_9)
    return melon_list

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



