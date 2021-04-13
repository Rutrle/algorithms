def linear_search(search_list, target):
    """
    returns position of target if found, if not return None
    """

    for index, value in enumerate(search_list):
        if value == target:
            return index

    return None


def verify(index):
    if index is not None:
        print(f"Target found at index {index}")
    else:
        print('Target was not found in the list')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

result = linear_search(numbers, 16)
verify(result)

result = linear_search(numbers, 7)
verify(result)