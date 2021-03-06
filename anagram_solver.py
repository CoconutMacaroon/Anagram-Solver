import re

VALID_CHARACTERS_REGEX = r'[^a-zA-Z0-9]'

def solve_anagram(word: str, dict_file_path: str):
    # solves an one-word anagram

    # read the dictionary file
    data = [word.lower() for word in open(dict_file_path, 'r').read().split('\n')]

    # make the word lowercase
    word = word.lower()

    # get rid of random characters in the word
    word = re.sub(VALID_CHARACTERS_REGEX, '', word)

    anagrams = []

    for i in range(len(data)):
        if str_sort(data[i]) == str_sort(word):
            anagrams.append(data[i])
    return anagrams 

str_sort = lambda text: ''.join(sorted(text))
