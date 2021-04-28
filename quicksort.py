numbers = [1, 5, 6, 4, 8, 3, 4, 6, 5, 2]


def quicksort(values):
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    print(f"{less_than_pivot},{pivot},{greater_than_pivot}")

    return quicksort(less_than_pivot)+[pivot]+quicksort(greater_than_pivot)


sorted_numbers = quicksort(numbers)
print(sorted_numbers)
