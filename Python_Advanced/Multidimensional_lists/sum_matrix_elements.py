rows, cols = [int(el) for el in input().split(", ")]

# matrix = [[int(el) for el in input().split(", ")] for i in range(rows)]
matrix = []
sum_nums = 0
for i in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    sum_nums += sum(numbers)
    matrix.append(numbers)

print(sum_nums)
print(matrix)
