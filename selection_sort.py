
numbers = [1, 5, 8, 44, 6, 45, 468]


def selection_sort(values):
    unsorted = values
    sorted_list = []

    while len(unsorted) > 0:
        print(unsorted, '\n', sorted_list)
        min_val = unsorted[0]
        for item in unsorted:
            if item < min_val:
                min_val = item

        unsorted.pop(unsorted.index(min_val))

        sorted_list.append(min_val)

    return sorted_list


print(selection_sort(numbers))
