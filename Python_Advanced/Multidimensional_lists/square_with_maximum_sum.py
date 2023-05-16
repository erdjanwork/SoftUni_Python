rows, cols = [int(el) for el in input().split(", ")]
matrix = [[int(el)for el in input().split(", ")] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = []

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        curr_el = matrix[row_idx][col_idx]
        el_below = matrix[row_idx + 1][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        diagonal_el = matrix[row_idx + 1][col_idx + 1]
        curr_sum_el = curr_el + el_below + next_el + diagonal_el

        if max_sum < curr_sum_el:
            max_sum = curr_sum_el
            sub_matrix = [[curr_el, next_el], [el_below, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
