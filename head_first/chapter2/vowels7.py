vowels = set('aeiou')
word = input('Type your word here to search for the vowels: ')

print(vowels.intersection(set(word)))

# How the book does it
# found = vowels.intersection(set(word))
# for vowel in found:
#     print(vowel)
