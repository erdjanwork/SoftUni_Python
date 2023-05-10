from collections import deque

people = deque()

water_quantity = int(input())

name = input()
while name != "Start":
    people.append(name)
    name = input()

command = input()


while command != "End":
    data = command.split()
    if len(data) == 1:
        litters = int(data[0])

        if water_quantity >= litters:
            water_quantity -= litters
            person = people.popleft()
            print(f"{person} got water")
        else:
            person = people.popleft()
            print(f"{person} must wait")
    else:
        litters_to_fill = int(data[1])
        water_quantity += litters_to_fill

    command = input()
print(f"{water_quantity} liters left")

