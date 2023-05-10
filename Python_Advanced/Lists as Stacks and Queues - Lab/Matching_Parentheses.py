stack_parentheses = []


text = input()

for idx in range(len(text)):
    if text[idx] == "(":
        stack_parentheses.append(idx)
    elif text[idx] == ")":
        start_position = stack_parentheses.pop()
        end_position = idx + 1
        print(text[start_position:end_position])
