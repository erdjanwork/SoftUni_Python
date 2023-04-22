num = int(input())
capacity = 255
litres_in_total = 0

for i in range(num):
    litres = int(input())
    litres_in_total += litres
    if litres_in_total > capacity:
        print("Insufficient capacity!")
        litres_in_total -= litres
        continue

print(litres_in_total)


# capacity = 255
#
# n = int(input())
# litres_in_total = 0
#     for i in range(n):
#         liters = int(input())
#         if liters + litres_in_total > capacity:
#             print('Insufficient capacity!')
#         else:
#             litres_in_total += litres_in_total
#
#
# print(litres_in_total)



