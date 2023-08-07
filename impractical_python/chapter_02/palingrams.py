'''Function to find 2-word palingrams from a provided word list'''
import load_dictionary

def find_palingrams():
    words = load_dictionary.load("words.txt")
    palingrams = []
    for word in words:
        rev_word = word[::-1]
        if len(word) > 1:
            for i in range(len(word)):
                if rev_word[i:] in words:
                    palingrams.append(word + word[::-i])
    return palingrams