n = int(input())
sum_of_letters = 0

for i in range(n):
    letter = input()
    sum_of_letters += ord(letter)

print(f"The sum equals: {sum_of_letters}")


