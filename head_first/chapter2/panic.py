phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# Use list manipulation methods so the final 2 print functions display "on tap"

for i in range(4):
    plist.pop()
plist.pop(0)
plist.pop(2)
temp = plist.pop(3)
plist.insert(2, temp)
temp = plist.pop()
plist.insert((len(plist) -1), temp)


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
