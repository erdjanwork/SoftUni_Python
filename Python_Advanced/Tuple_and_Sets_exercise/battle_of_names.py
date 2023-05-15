ood_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(l) for l in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        ood_set.add(ascii_sum_of_name)

if sum(ood_set) > sum(even_set):
    print(*ood_set.difference(even_set), sep=", ")

else:
    print(*ood_set.symmetric_difference(even_set), sep=', ')

