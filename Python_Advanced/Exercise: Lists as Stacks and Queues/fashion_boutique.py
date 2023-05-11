from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())

used_racks = 1
current_rack_space = rack_capacity

while clothes:
    cloth = clothes.pop()

    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        used_racks += 1
        current_rack_space = rack_capacity - cloth

print(used_racks)
