"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as raw_file:
        string_file = raw_file.read()
    return string_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
    chains = {}
    for index, current_word in enumerate(words):
        # check if we can build the next bigram and value key-value pair
        # if we are too close to the end of the list stop
        if index == len(words) - 2:
            break
        pair_word = words[index + 1]
        bigram = (current_word, pair_word)
        option_word = words[index + 2]
        current_value = chains.get(bigram)
        # check dictionary chains[bigram]
        if current_value is None:
            chains[bigram] = [option_word]
        else:
            chains[bigram].append(option_word)
    return chains


# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, ..., wordN)
#     and the value would be a list of the word(s) that follow those N
#     words in the input text. The length of the tuple / N-gram will be
#     decided based on user input

#     For example:

#         >>> chains = make_chains("hi there mary hi there juanita")

#     Each bigram (N=2) (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']

#         >>> chains[('there','juanita')]
#         [None]
#     """

#     words = text_string.split()
#     chains = {}

    # loop to ensure length is int & greater than 1 / less than length of words
    # n_gram_length = input(...)

#     for index, current_word in enumerate(words):
#         # check if we can build the next bigram and value key-value pair
#         # if we are too close to the end of the list stop
#         if index == len(words) - n_gram_length:
#             break

#         pair_word = words[index + 1]
#         bigram = (current_word, pair_word)
#         option_word = words[index + 2]
#         current_value = chains.get(bigram)
#         # check dictionary chains[bigram]
#         if current_value is None:
#             chains[bigram] = [option_word]
#         else:
#             chains[bigram].append(option_word)
#     return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    # pick random bigram (key from dict)
    chains_key_list = list(chains.keys())
    current_bigram = choice(chains_key_list)
    words.extend(current_bigram)
    while chains.get(current_bigram):  # None returns false
        second_word_in_bigram = current_bigram[1]
        # pick random value from that bigram and adds to the words
        next_word = choice(chains[current_bigram])
        words.append(next_word)
        # link second word with the new word to make the next bigram
        current_bigram = (second_word_in_bigram, next_word)
    return " ".join(words)


# input file as the second argument to command line (ie python3 markov.py file)
input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
