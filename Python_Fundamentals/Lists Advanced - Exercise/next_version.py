# def new_version(a, b, c):
#     c += 1
#     if c == 10:
#         b = 0
#
#
major, minor, patch = [int(x) for x in input().split('.')]

patch += 1
if patch == 10:
    patch = 0
    minor += 1
    if minor == 10:
        minor = 0
        major += 1

print(f"{major}.{minor}.{patch}")
