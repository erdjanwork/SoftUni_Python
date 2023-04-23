def get_even_and_odd_sums(numbers):
    even_sum = 0
    odd_sum = 0
    for digit_as_str in numbers:
        digit = int(digit_as_str)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number = input()
print(get_even_and_odd_sums(number))