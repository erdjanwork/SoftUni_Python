budget = int(input())

prices = input()

while prices != 'End':
    prices_now = int(prices)

    budget -= prices_now

    if budget < 0:
        print(f"You went in overdraft!")
        exit()
    prices = input()

print("You bought everything needed.")
