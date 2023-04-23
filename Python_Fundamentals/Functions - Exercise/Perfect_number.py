def is_perfect(number):
    proper_divisor = []
    for current_num in range(1, number):
        if number % current_num == 0:
            proper_divisor.append(current_num)
    if sum(proper_divisor) == number:
        return True
    return False


number = int(input())

if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")