counter = int(input())
word = input()

sentence_list = []

for i in range(counter):
    sentence = input()
    sentence_list.append(sentence)
print(sentence_list)

for i in range(len(sentence_list) - 1, -1, -1):
    element = sentence_list[i]
    if word not in element:
        sentence_list.remove(element)
print(sentence_list)