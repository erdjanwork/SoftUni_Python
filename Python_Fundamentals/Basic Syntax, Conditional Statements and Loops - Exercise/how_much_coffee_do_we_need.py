counter = 0

while True:
    line = input()
    if line == 'END':
        break

    if line == "dog" or line == 'cat' or line == 'coding' or line == 'movie':
        counter += 1

    elif line == 'DOG' or line == 'CAT' or line == 'CODING' or line == 'MOVIE':
        counter += 2

if counter > 5:
    print('You need extra sleep')
else:
    print(counter)
