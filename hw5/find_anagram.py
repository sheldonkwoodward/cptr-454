# sheldon woodward
# 2/10/19

from collections import defaultdict


def find_anagram(words):
    """
    Takes a list of words and finds all anagram sets within the list. Instead of using a standard python dictionary
    as a hashmap, this method uses the defaultdict object. defaultdict is more efficient than a standard
    Python dictionary when you need to perform a key lookup and then create a new key-value pair if it does not
    already exist.

    :param words: A list of words to find anagrams of.
    :return: Returns a list of anagram lists.
    """
    # dictionary of anagrams
    anagrams = defaultdict(list)
    # check every word from word list
    for word in words:
        # lookup the sorted characters of a word as a key in anagrams. if the key does not exist,
        # it will automatically be created with its value as a blank list.
        anagrams[''.join(sorted(word))].append(word)
    # return a list of all of the anagram lists
    return anagrams.values()

