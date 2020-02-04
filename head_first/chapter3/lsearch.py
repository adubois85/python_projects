def search_for_letters(phrase: str, letters: str) -> set:
    """Returns set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


# search_for_letters()
