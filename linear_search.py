def linear_search(search_list, target):
    """
    returns position of target if found, if not return None
    """

    for index, value in enumerate(search_list):
        if value == target:
            return index

    return None


my_list = ['a', 'b', 'c', 'd', 'e']

print(linear_search(my_list, 'd'))
