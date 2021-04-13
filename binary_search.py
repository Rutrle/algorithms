def binary_search(search_list, target):
    first = 0
    last = len(search_list)-1

    while first <= last:
        midpoint = (first + last)//2

        if search_list[midpoint] == target:
            return midpoint
        elif search_list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print('Target was not found in the list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = binary_search(numbers, 16)
verify(result)

result = binary_search(numbers, 7)
verify(result)
