import re

number = input()
pattern = r'\+359 2 \d{3} \d{4}| \+359-2-\d{3}-\d{4}\b'

result = re.findall(pattern, number)

print(*result, sep=', ')
