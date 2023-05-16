rows = int(input())

# matrix = [[int(el) for el in input().split(", ")] for i in range(rows)]
flatten = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    flatten.extend(inner_list)
# for list_el in matrix:
#     flatten.extend(list_el)

# for row_idx in range(len(matrix)):
#     for col_idx in range(len(matrix[row_idx])):
#         curr_el = matrix[row_idx][col_idx]
#         flatten.append(curr_el)

print(flatten)