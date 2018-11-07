phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# Use slice notation to transform the initial phrase to the phrase "on tap"
new_phrase = plist[1:3]
new_phrase.extend(plist[5:3:-1])
new_phrase.extend(plist[-5: -7: -1])
new_phrase = ''.join(new_phrase)

# And how the book does it
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)
