words = input().split()
result = [x for x in words if len(x) % 2 == 0]
print("\n".join(result)) # for word in result:
                         # print(result)
                         