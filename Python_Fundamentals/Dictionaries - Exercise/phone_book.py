contact = {}

n = 0

while True:
    line = input()
    parts = line.split("-")
    if len(parts) == 1:
        n = int(line)
        break

    name = parts[0]
    number = parts[1]

    contact[name] = number


for _ in range(n):
    name = input()
    if name in contact:
        print(f"{name} -> {contact[name]}")
    else:
        print(f"Contact {name} does not exist.")