substrings = input().split(", ")
strings = input().split(', ')

remaining_strings = []

for substr in substrings:
    for word in strings:
        found_substr = substr in word
        if found_substr:
            remaining_strings.append(substr)
            break

print(remaining_strings)


