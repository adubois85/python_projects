vowels = ['a', 'e', 'i', 'o', 'u']
found = []
word = input('Type your word here to search for the vowels: ')

for letter in word:
    if letter in vowels and letter not in found:
        found.append(letter)
for vowel in found:
    print(vowel)
