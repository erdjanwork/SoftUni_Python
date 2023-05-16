matrix = []
rows = int(input())
for i in range(rows):
    numbers = [int(x)
               for x in input().split(", ")
               if int(x) % 2 == 0]
    # even_numbers = [num for num in numbers if num % 2 == 0]
    matrix.append(numbers)

print(matrix)