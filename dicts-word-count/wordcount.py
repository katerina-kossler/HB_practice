
def count_words(filename):
    """ set up function to count the words in the textfile """

    #create empty dictionary of words
    words_dictionary = {}    
    poem = open(filename)
    for line in poem:
        line = line.rstrip() # removes trailing white space
        list_of_words = line.split(" ") # breaks line into a list of words 
        
        for word in list_of_words: 
            # iterate over list of words to add to dict
            words_dictionary[word] = words_dictionary.get(word, 0) + 1
            # checks for key of word and sets count of 0 if not present
            #adds a count of one to the value for every iteration of the 
            #same word 
    return words_dictionary

print(count_words("test.txt"))
print(count_words("twain.txt"))
