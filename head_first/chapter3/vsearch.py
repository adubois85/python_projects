def search_for_vowels():
    vowels = set('aeiou')
    word = input('Type your word here to search for the vowels: ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


search_for_vowels()
