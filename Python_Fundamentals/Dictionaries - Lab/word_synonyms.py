count = int(input())
synonym = {}

for _ in range(count):
    key = input()
    value = input()
    if key not in synonym:
        synonym[key] = []
    synonym[key].append(value)


for word, all_synonyms in synonym.items():
    print(f"{word} - {', '.join(all_synonyms)}")