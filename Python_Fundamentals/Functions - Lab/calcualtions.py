def calculation(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a // b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


input_operator = input()
num_1 = int(input())
num_2 = int(input())

print(calculation(a=num_1, b=num_2, operator=input_operator))


