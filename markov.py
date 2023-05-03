"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    whatev_works = open(file_path)
    whole_file = whatev_works.read().split()
    return whole_file

    return 'Contents of your file as one long string'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    tuple_list = []

    for idx in range(len(text_string)-2): #hint= -2
        new_value = idx + 1
        second_value = idx + 2
        #grab both idx+1 and idx+2
        key_tuple = (text_string[idx], text_string[new_value])

        if key_tuple not in chains: 
            chains[key_tuple]  = [text_string[second_value]]

        else:
            chains[key_tuple].append(text_string[second_value])

    for key, value in chains.items():
        print(key, ':', value)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    for key in chains:
        key = [key]

    

    phrase = choice(list(chains.keys()))
    print (phrase)

    # words.append()
    # print(words)

    # return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
