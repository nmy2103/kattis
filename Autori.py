names = input()
initials = names[0]
for letter in range(len(names)):
    if names[letter] == '-':
        initials += names[letter + 1]
print(initials)
