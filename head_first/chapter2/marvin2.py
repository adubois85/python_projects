
# You can iterate over a list as-is (and other data structures?)
paranoid_android = 'Marvin, the Paranoid Android'
letters = list(paranoid_android)
# You can also use slice notation when iterating over a list
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t' * 2, char)
print()
for char in letters[12:20]:
    print('\t' * 3, char)
