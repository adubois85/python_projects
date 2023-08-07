'''Function to find 2-word palingrams from a provided word list'''
import load_dictionary

def find_palingrams():
    words = load_dictionary.load("words.txt")
    palingrams = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            # I misunderstood the assignment and was making lots of unnnecessary comparisons
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    palingrams.append(f"{word} {rev_word[end - i:]}")
    return palingrams