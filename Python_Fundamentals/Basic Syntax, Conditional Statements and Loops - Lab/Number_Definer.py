a = float(input())

if a == 0:
    print("zero")
elif a > 0:
    if a < 1:
        print("small positive")
    elif a > 1000000:
        print("large positive")
    else:
        print("positive")

else:
    if abs(a) < 1:
        print("small negative")
    elif abs(a) > 1000000:
        print("large negative")
    else:
        print("negative")