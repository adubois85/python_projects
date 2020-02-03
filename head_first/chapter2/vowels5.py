vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Type your word here to search for the vowels: ')
found = {}
for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
