words = [word.lower() for word in input().split()]
default = 0

dictionary = dict.fromkeys(words, default)
for word in words:
    dictionary[word] += 1

for word, count in dictionary.items():
    if count % 2 != 0:
        print(word, end=' ')
