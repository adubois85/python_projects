'''Takes a single user word as input and returns its anagrams'''
import load_dictionary

def find_anagrams():
    anagrams = []
    words = load_dictionary.load("../chapter_02/words.txt")
    user_word = input("Enter a single word to see its anagrams.\n").lower()
    user_word_sorted = sorted(user_word)
    for word in words:
        if word != user_word:
            sorted_word = sorted(word)
            if sorted_word == user_word_sorted:
                anagrams.append(word)
    return anagrams
