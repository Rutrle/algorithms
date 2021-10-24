def sum_natural_nums(number):
    if number <= 1:
        return number
    else:
        return sum_natural_nums(number-1)+number


print(sum_natural_nums(10))
