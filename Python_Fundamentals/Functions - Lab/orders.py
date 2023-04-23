def orders(order, quantity):
    bill = 0
    if order == "coffee":
        bill = quantity * 1.50
    elif order == "coke":
        bill = quantity * 1.40
    elif order == "water":
        bill = quantity * 1.00
    elif order == "snacks":
        bill = quantity * 2.00
    return bill


product = input()
quantity = int(input())
total = orders(product, quantity)

print(f"{total:.2f}")