from collections import deque

number = deque(input().split())

for _ in range(len(number)):
    print(number.pop(), end=' ')