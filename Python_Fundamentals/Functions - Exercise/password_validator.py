def is_valid_length(password):
    return 6 <= len(password) <= 10


def contains_alpha_numeric_chars(password):
    return password.isalnum()


def contains_at_least_two_digits(password):
    digits_counter = 0
    for ch in password:
        if ch.isdigit():
            digits_counter += 1

    return digits_counter >= 2


input_password = input()
is_valid = True

if not is_valid_length(input_password):
    is_valid = False
    print("Password must be between 6 and 10 characters")

if not contains_alpha_numeric_chars(input_password):
    is_valid = False
    print("Password must consist only of letters and digits")

if not contains_at_least_two_digits(input_password):
    is_valid = False
    print("Password must have at least 2 digits")

if is_valid:
    print("Password is valid")