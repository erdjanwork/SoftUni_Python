num = int(input())
odd = []
even = []
positive = []
negative = []

for i in range(num):
    numbers = int(input())
    if numbers >= 0:
        positive.append(numbers)
    else:
        negative.append(numbers)
    if numbers % 2 == 0:
        even.append(numbers)
    else:
        odd.append(numbers)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)

