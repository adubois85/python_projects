def search_for_vowels(phrase: str) -> set:
    """Returns set of vowels found in 'phrase'."""
    return set('aeiou').intersection(set(phrase))


def search_for_letters(phrase: str, letters: str = 'aeiou') -> set:
    """Returns set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
