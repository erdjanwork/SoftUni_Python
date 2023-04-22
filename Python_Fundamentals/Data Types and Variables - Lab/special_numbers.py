number = int(input())

for num in range(1, number + 1):
    is_special = False
    num_as_str = str(num)
    sum_of_digits = 0

    for char in num_as_str:
        sum_of_digits += int(char)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True
    print(f"{num} -> {is_special}")