'''Progressively builds an anagram from user-inputted name'''
from collections import Counter
import pprint as pp
import re
import sys

import load_dictionary

# This should strip everything that isn't one of the 26 letters from the name
name = input("Enter a full name and get to building an anagram of it.\n")
name = re.findall(r'[a-zA-Z]+', name.lower())
name = Counter("".join(name))
words = load_dictionary.load("../chapter_02/words.txt")
# 'a' and 'I' are valid words for anagrams
words.append("a")
words.append("i")

def main():
    name_limit = len(name)
    anagram_phrase = []
    phrase_limit = sum(map(len, anagram_phrase))
    while phrase_limit < name_limit:
        possible_anagrams = find_anagrams(name, words)
        print(*possible_anagrams, sep='\n')
        print(f'Possible anagrams remaining: {len(possible_anagrams)}')
        print(f'There are {len(name)} remaining letters.  They are: {name}')
        print(f'The current anagram is "{" ".join(anagram_phrase)}"')


def find_anagrams(name, words: list) -> list:
    name = Counter(name)
    anagrams = []
    for word in words:
        count = Counter(word)
        temp = ''
        for letter in word:
            if count[letter] <= name[letter]:
                temp += letter
        if Counter(temp) == count:
            anagrams.append(word)
    return anagrams

# I'm trying really hard to follow along with the examples in the book, but
# the way he organizes code and breaks down the problem is often odd to me.
def process_choice():
    word_choice = input("Choose the next word for the anagram, or hit Enter to start over, else '#' to end")
    if word_choice == '':
        sys.exit()
    elif word_choice == '#':
        main()
    word_choice = word_choice.lower()
    
