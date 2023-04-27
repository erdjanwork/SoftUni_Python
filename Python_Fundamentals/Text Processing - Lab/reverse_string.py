result = ''
while True:
    line = input()
    if line == "end":
        break
    result = ''
    for word in reversed(line):
        result += word

    print(f'{line} = {result}')