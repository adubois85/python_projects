'''Find all the palindromes in a list of words'''
import load_dictionary

def find_palindromes() -> list:
    words = load_dictionary.load("words.txt")
    palindromes = []
    for word in words:
        # single letters aren't really palindromes
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    print(f"\nNumber of palindromes found = {len(palindromes)}\n")
    print(*palindromes, sep='\n')
    return palindromes
