
while True:
    names = input()
    if names == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if names == "Voldemort":
        print("You must not speak of that name!")
        exit()
    if len(names) < 5:
        print(f"{names} goes to Gryffindor.")
    elif len(names) == 5:
        print(f"{names} goes to Slytherin.")
    elif len(names) == 6:
        print(f"{names} goes to Ravenclaw.")
    else:
        print(f"{names} goes to Hufflepuff.")

