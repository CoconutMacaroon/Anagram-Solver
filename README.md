# Anagram-Solver
This is an anagram solver. It takes an anagram and solves the anagram.  

It takes an input via the `input()` function, and then loops though a dictionary file looking for matches.  
Note that `main.py` references a dictionary file (`dictionary.txt`), but that is not in this repository. When `main.py` is run, a dictionary file named `dictionary.txt` will need to be in the same directory as `main.py`. To see how long it took to find the anagrams, use the `-d` flag with the `main.py`. For example, `python3 main.py -d`.
# Running the program  
Once the program is started, enter the scrambeled anagram, and it will print out all results.  
# Flags  
To use flags, type the flag after the program name. For example, to use the `-d` flag, you could use, `python main.py -d`.  
  
`-d` Prints time it took to find all anagrams.
