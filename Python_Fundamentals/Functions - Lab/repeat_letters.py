def repeat(letters, counter):
    word = letters * counter
    return word


words = input()
num = int(input())
result = lambda a, b: words * num
print(result(words, num))



