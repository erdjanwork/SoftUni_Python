rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(el) for el in input().split()] for i in range(rows)]

result = []

for col_idx in range(cols):
    sum_cols = 0
    for row_idx in range(rows):
        sum_cols += matrix[row_idx][col_idx]
    result.append(sum_cols)

[print(x) for x in result]


