# from math import ceil
#
# number_of_people = int(input())
# capacity = int(input())
#
# courses = int(number_of_people / capacity)
#
# if number_of_people % capacity == 0:
#     courses += 1
#
# courses = ceil(number_of_people / capacity)
#
# print(courses)
from math import ceil

number_of_people = int(input())
capacity = int(input())

courses = ceil(number_of_people / capacity)

print(courses)