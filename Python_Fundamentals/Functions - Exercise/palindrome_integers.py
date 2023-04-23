counter = int(input())
even = []
odd = []
positive = []
negative = []

for i in range(counter):
    number = int(input())
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative.append(number)
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
command = input()

if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)

