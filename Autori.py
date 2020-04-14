# Natasha M. Yamane
# Kattis: Autori

# April 13, 2020

names = input()
initials = names[0]
for letter in range(len(names)):
    if names[letter] == '-':
        initials += names[letter + 1]
print(initials)
