reservations = set()

for _ in range(int(input())):
    reservation = input()
    reservations.add(reservation)

while True:
    line = input()
    if line == "END":
        break
    if line in reservations:
        reservations.remove(line)

print(len(reservations))
for num in sorted(reservations):
    print(num)