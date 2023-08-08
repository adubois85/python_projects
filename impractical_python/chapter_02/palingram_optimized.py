'''Function to find 2-word palingrams from a provided word list'''
# import time
import load_dictionary
import pprint as pp

def find_palingrams():
    # sets are magical
    words = set(load_dictionary.load("2of4brif.txt"))
    palingrams = []
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    palingrams.append(f"{word} {rev_word[end - i:]}")
                if word[:end - i] == rev_word[i:] and rev_word[:i] in words:
                    palingrams.append(f"{rev_word[:i]} {word}")
    return sorted(palingrams)

# start_time = time.time()
palingrams = find_palingrams()
# end_time = time.time()
# print(f"The runtime for this function was {start_time - end_time}")

pp.pprint(palingrams)
