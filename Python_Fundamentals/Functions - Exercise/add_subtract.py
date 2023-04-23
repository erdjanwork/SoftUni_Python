def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

sum_of_numbers = add(num_1, num_2)

print(subtract(sum_of_numbers, num_3))