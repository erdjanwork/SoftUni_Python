num = int(input())
train = [0] * num

# for i in range(num):
#     trains.append(0)


command = input()
while command != 'End':
    action = command.split()[0]
    if action == "add":
        n_people = int(command.split()[1])
        train[-1] += n_people
    elif action == "insert":
        seat = int(command.split()[1])
        n_people = int(command.split()[2])
        train[seat] += n_people
    elif action == "leave":
        seat = int(command.split()[1])
        n_people = int(command.split()[2])
        train[seat] -= n_people
    command = input()

print(train)