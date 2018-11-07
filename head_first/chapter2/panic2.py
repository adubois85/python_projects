phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#Use slice notation to transform the initial phrase to the phrase "on tap"
new_phrase = plist[1:3]
new_phrase.extend(plist[5:3:-1])
new_phrase.extend(plist[-5: -7: -1])
new_phrase = ''.join(new_phrase)

print(plist)
print(new_phrase)
