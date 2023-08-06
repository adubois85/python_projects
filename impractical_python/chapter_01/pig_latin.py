def pig_latinize() -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    # No guardrails since this is really just a toy example
    word = input('Enter a single word\n')
    if word[0].lower() in vowels:
        word = word + 'way'
    elif (word[0].lower() == 't' and word[1].lower() == 'h'):
        word = word[2:] + 'th' + 'ay'
    else:
        word = word[1:] + word[0].lower() + 'ay'
    return word
