def smallest_of_numbers(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number:
            min_number = num
    return min_number

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(smallest_of_numbers([num_1, num_2, num_3]))


