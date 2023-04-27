products = {}
data = input().split()

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i + 1])
    products[key] = value

searched_prod = input().split()
for searched_prod in searched_prod:
    if searched_prod in products.keys():
        print(f"We have {products[searched_prod]} of {searched_prod} left")
    else:
        print(f"Sorry, we don't have {searched_prod}")