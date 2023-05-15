n, m = [int(num) for num in input().split()]
set_n = {int(input()) for _ in range(n)}
set_m = {int(input()) for _ in range(m)}


print(*set_n.intersection(set_m), sep='\n')