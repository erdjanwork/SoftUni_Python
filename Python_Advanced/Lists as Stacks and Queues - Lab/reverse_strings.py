text = input()

stack_text = list(text)

while stack_text:
    removed_string = stack_text.pop()
    print(removed_string, end="")

