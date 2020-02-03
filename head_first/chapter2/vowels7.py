vowels = set('aeiou')
word = input('Type your word here to search for the vowels: ')

print(vowels.intersection(set(word)))

# for letter in word:
#     if letter in vowels and letter not in found:
#         found.append(letter)
# for vowel in found:
#     print(vowel)
