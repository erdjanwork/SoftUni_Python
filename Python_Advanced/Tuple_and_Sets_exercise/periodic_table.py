# chemicals = {input().split() for _ in range(int(input()))}

chemicals = set()

for _ in range(int(input())):
    for el in input().split():
        chemicals.add(el)

print(*chemicals, sep="\n")
