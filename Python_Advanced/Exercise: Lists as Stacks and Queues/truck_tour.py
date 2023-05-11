from collections import deque

pumps_data = deque([[int(x)for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
gas_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_tank += petrol

    if gas_tank >= distance:
        gas_tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_tank = 0


print(index)
