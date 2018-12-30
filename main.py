def main():
    from sys import argv
    from time import time
    # load the dictionary file into the word_dictionary
    word_dictionary = []
    current_time = time()
    for word in open('dictionary.txt', 'r'):
        word_dictionary.append(word.lower().strip())
    if "-d" in argv:
        print("[INFO] Took " + str(time() - current_time) + " seconds to load dictionary")

    while True:
        anagram = input("Enter an anagram to be solved: ").lower()
        is_anagram_found = False
        current_time = time()
        for word in word_dictionary:
            if (len(word) == len(anagram)) and (sorted(anagram) == sorted(word)) and not (word == anagram):
                is_anagram_found = True
                print(word)
        if not is_anagram_found:
            print("Bummer. No anagrams found.")
        if "-d" in argv:
            print("[INFO] Took " + str(time() - current_time) + " seconds to find anagram matches")


if __name__ == "__main__":  # only run the program if started directly, rather than from a module
    main()
else:
    print("[INFO] This file was imported as a module, so code will not be excecuted. To start program, run 'main()'.")
    
