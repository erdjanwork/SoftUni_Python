numbers = input().split()

for i in range(len(numbers)):
    reversed_numbers = numbers.pop()
    print(reversed_numbers, end=" ")
