from math import ceil
numbers = [int(x) for x in input().split(', ')]

low_boundary = 1
high_boundary = 10

groups_count = ceil((max(numbers) / 10))
for idx in range(1, groups_count + 1):
    # filtering
    # print
    grouped_numbers = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * idx}'s: {grouped_numbers}")

    low_boundary += 10
    high_boundary += 10
