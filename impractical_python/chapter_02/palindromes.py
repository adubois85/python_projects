'''Find all the palindromes in a list of words'''
import load_dictionary

def find_palindromes() -> list:
    words = load_dictionary.load("words.txt")
    palindromes = []
    for word in words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes
