n = int(input())

stack = []

for i in range(n):
    command_args = input().split()
    command = command_args[0]

    if command == '1':
        number = int(command_args[1])
        stack.append(number)

    elif command == '2':
        if stack:
            stack.pop()

    elif command == '3':
        if stack:
            print(max(stack))

    elif command == '4':
        if stack:
            print(min(stack))

stack.reverse()

print(*stack, sep=", ")




