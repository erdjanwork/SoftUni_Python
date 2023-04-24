rooms = int(input())
free_chairs = 0
available_chairs = True
for room in range(1, rooms + 1):
    chairs, visitors_as_str = input().split()
    visitor = int(visitors_as_str)

    if visitor > len(chairs):
        needed_chairs = visitor - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        available_chairs = False

    else:
        free_chairs_by_row = len(chairs) - visitor
        free_chairs += free_chairs_by_row

if available_chairs:
    print(f"Game On, {free_chairs} free chairs left")
