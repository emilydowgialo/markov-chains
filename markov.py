from random import choice

import sys

#added sys.argv for an easy way to import files via the command line
filename = sys.argv[1]
print filename



def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    #This should be a variable that contains your file text as one long string
    return contents 


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}


    words = text_string.split()

    #looping over a list by index by looping over a range
    #range is minus 2 because when we reach the end of the list we add 2 to the index
    for i in range(len(words) - 2):
        #binding key variable to first two words in the string
        key = (words[i], words[i + 1])
        #if the key is in the dictionary (chains), we add the value of the third word
        if key in chains:
            #this is the third word, which will be added as the value of the key
            chains[key].append(words[i+2])
        else:
            #if key not in dictionary, add the key and value to the dictionary
            chains[key] = [words[i+2]]


    return chains
 

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    
    #random choice of key from dictionary
    key = choice(chains.keys())
    #text is the tuple key
    text = key[0] + " " + key[1]
    
    while True:
       
        #this is the list of values, which we are checking for error
        #this is the key error: if key not in dictionary
        options_for_next_word = chains.get(key, None)

        #if key not in dictionary, break out of the loop
        #if not options_for_next_word:
        if options_for_next_word == None:
            break
        
        #this is a random element from the list that is the value for the previous key
        random_item_from_list = choice(options_for_next_word)

        #new key tuple
        new_key = (key[1], random_item_from_list)
        key = new_key

        # taking excisting text adding new word choosen from dictionary
        text = text + " " + random_item_from_list

    
    return text




# Open the file and turn it into one long string
input_text = open_and_read_file(filename)

# Get a Markov chain
chains = make_chains(input_text)
# print chains 

# Produce random text
random_text = make_text(chains)

print random_text
