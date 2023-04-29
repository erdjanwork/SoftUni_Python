from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "-" + "_"

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    contains_forbidden_char = all(char in allowed_chars for char in username)
    if not contains_forbidden_char:
        continue

    print(username)
