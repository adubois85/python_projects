'''Takes a single user word as input and returns its anagrams'''
import load_dictionary

def find_anagrams():
    anagrams = []
    words = load_dictionary.load("../chapter_02/words.txt")
    user_word = input("Enter a single word to see its anagrams.\n")
    user_word = sorted(user_word.lower())
    for word in words:
        sorted_word = sorted(word)
        if sorted_word == user_word:
            anagrams.append(word)
    return anagrams
