def search_for_vowels(word: str) -> set:
    """Propmpts user for a word and returns any vowels in it (but not 'y')"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


search_for_vowels()
