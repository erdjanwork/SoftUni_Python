from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if quantity_food >= order:
        orders.popleft()
        quantity_food -= order
    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print(f'Orders complete')





