n = int(input())
cars = set()

for _ in range(n):
    directions, number = input().split(", ")
    if directions == "IN":
        cars.add(number)
    elif directions == "OUT":
        cars.remove(number)

if cars:
    print(*cars, sep='\n')
else:
    print('Parking Lot is Empty')