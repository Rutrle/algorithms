
numbers = [1, 5, 8, 6, 4, 7, 2, 6]


def normal_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def recursive_sum(numbers):
    if not numbers:
        return 0

    remaining = recursive_sum(numbers[1:])
    print(f'remaining sum: {remaining}, numbers:{numbers} ')

    return numbers[0] + remaining


print(normal_sum(numbers))

print(recursive_sum(numbers))
