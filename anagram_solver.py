import re

def solve_anagram(word, dict_file):
    # solves an one-word anagram

    # read the dictionary file
    data = [word.lower() for word in open(dict_file, 'r').read().split('\n')]

    # make the word lowercase
    word = word.lower()

    # get rid of random characters in the word
    word = re.sub(r'[^a-zA-Z0-9]', '', word)

    anagrams = []

    for i in range(len(data)):
        if str_sort(data[i]) == str_sort(word):
            anagrams.append(data[i])
    return anagrams 

def str_sort(string):
    return ''.join(sorted(string))
