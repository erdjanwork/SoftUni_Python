text = input()
result = text[0]

for ch in text:
    if ch == result[-1]:
        continue
    result += ch

print(result)