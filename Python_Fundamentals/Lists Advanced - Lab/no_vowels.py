word = input()
no_vowels = [el for el in word if el.lower() not in ['a', 'o', 'u', 'i', 'e']]
print("".join(no_vowels))