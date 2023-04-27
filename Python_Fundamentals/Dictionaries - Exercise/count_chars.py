words = input().split()

counter = {}

for word in words:
    for ch in word:
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 1

for ch, count in counter.items():
    print(f"{ch} -> {count}")