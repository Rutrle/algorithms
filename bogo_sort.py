import random
import sys


numbers = [1, 5, 8, 44, 6, 45, 468]


def is_sorted(values):
    for index in range(len(values)-1):
        if values[index] > values[index+1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        print(values)
        attempts += 1

    print(attempts)
    return values


print(bogo_sort(numbers))
