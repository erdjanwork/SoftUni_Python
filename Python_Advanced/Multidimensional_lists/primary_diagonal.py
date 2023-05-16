rows = int(input())
matrix = [[int(el) for el in input().split()] for i in range(rows)]

sum_diagonal = 0
for idx in range(rows):
    sum_diagonal += matrix[idx][idx]

print(sum_diagonal)


