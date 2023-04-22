num_of_snowballs = int(input())

best = float('-inf')
output = ''
for i in range(num_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight // time) ** quality
    if result > best:
        best = result
        output = f"{weight} : {time} = {result} ({quality})"

print(output)
