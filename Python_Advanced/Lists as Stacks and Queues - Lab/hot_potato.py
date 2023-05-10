from collections import deque


names = deque(input().split())
rotator = int(input()) - 1

while len(names) > 1:
    names.rotate(-rotator)
    lost_name = names.popleft()
    print(f"Removed {lost_name}")

print(f"Last is {names.popleft()}")