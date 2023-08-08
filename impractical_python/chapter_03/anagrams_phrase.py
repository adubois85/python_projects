'''Progressively builds an anagram from user-inputted name'''
from collections import Counter
import load_dictionary
import re

# This should strip everything that isn't one of the 26 letters from the name
name = input("Enter a full name and get to building an anagram of it.\n")
name = re.findall(r'[a-zA-Z]+', name.lower())
name = Counter("".join(name))
words = load_dictionary.load("../chapter_02/words.txt")

def main():
    pass

def find_anagrams():
    pass

def process_choice():
    pass
