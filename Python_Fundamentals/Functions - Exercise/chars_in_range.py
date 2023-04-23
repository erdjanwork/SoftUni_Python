def get_chars_in_range(start, end):
    result = []
    for num in range(ord(start) + 1, ord(end)):
        result.append(chr(num))

    return result


start_char = input()
end_char = input()

result_chars = get_chars_in_range(start_char, end_char)
print(' '.join(result_chars))