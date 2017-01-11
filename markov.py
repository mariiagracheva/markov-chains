#from random import choice
import random
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    data_text = open(file_path, 'r').read()

    return data_text


def make_chains(text_string, n_gram):
    """Takes input text as string and size of token; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()

    #extend our string with two first words
    words = words[:] + words[:n_gram]
    chains = {}
    key_chains = []

    # create all n-gramms from text_string
    for index in xrange(len(words) - n_gram):
        key_chains = tuple(words[index:index+n_gram])
        if key_chains in chains:
            chains[key_chains].append(words[index + n_gram])
        else:
            chains[key_chains] = [words[index+n_gram]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = []
    #start with a random key from chains
    random_key = random.sample(chains, 1)[0]
    #add all words from key to text list
    for key in random_key:
        text.append(key)

    # add next word to text, create new next_key
    next_key = random_key
    while len(text) < 10:
        next_word = random.choice(chains[next_key]) #string
        text.append(next_word) #list
        next_key = next_key[1:] + tuple([next_word])

    return " ".join(text)


#input_path = "green-eggs.txt"
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
size_n_gram = int(raw_input("Enter size of n_grams: "))
chains = make_chains(input_text, size_n_gram)

# Produce random text
random_text = make_text(chains)

print random_text
