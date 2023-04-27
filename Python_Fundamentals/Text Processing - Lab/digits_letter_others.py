word = input()

letters = ''
digits = ''
others = ''

for char in word:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        others += char

print(digits)
print(letters)
print(others)