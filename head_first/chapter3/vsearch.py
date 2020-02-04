def search_for_vowels():
    """Propmpts user for a word and returns any vowels in it (but not 'y')"""
    vowels = set('aeiou')
    word = input('Type your word here to search for the vowels: ')
    print(vowels.intersection(set(word)))

    # found = vowels.intersection(set(word))
    # for vowel in found:
    #     print(vowel)


search_for_vowels()
