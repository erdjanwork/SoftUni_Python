orders = int(input())

total = 0
for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())

    if 0.01 > price_per_capsule or price_per_capsule > 100.00:
        continue

    if days < 1 or days > 31:
        continue

    if 1 > capsules_needed or capsules_needed > 2000:
        continue

    price = days * capsules_needed * price_per_capsule
    total += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")