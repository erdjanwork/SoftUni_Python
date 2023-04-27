banned_word = input().split(', ')
text = input()
for word in banned_word:
    text = text.replace(word, "*"*len(word))
print(text)