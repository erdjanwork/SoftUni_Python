numbers = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(numbers)):
    beggar_index = idx % beggars_count
    num = int(numbers[idx])
    beggars[beggar_index] += num

print(beggars)


