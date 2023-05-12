numbers = [float(x) for x in input().split()]

nums_and_occurrences = {}
for num in numbers:
    if num not in nums_and_occurrences:
        nums_and_occurrences[num] = 0
    nums_and_occurrences[num] += 1

[print(f"{key} - {value} times") for key, value in nums_and_occurrences.items()]