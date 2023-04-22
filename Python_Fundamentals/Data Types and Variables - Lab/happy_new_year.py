year = int(input())
year_as_str = str(year)


while len(year_as_str) != len(set(year_as_str)):
    year_as_str = str(year)
    year += 1
print(year)
