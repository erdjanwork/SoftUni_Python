# print({*input() for _ in range(int(input)))}, sep="\n"}

names = set()
for _ in range(int(input())):
    name = input()
    names.add(name)

for name in names:
    print(name)
# print(*names, sep="\n")
