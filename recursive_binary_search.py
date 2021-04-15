def recursive_binary_search(search_list, target):
    if len(search_list) == 0:
        return False
    else:
        midpoint = len(search_list)//2

    if search_list[midpoint] == target:
        return True
    else:
        if search_list[midpoint] < target:
            return recursive_binary_search(search_list[midpoint+1:], target)
        else:
            if search_list[midpoint] < target:
                return recursive_binary_search(search_list[:midpoint], target)


def verify(result):
    print(f"target found: {result}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = (recursive_binary_search(numbers, 12))
verify(result)


result = (recursive_binary_search(numbers, 6))
verify(result)
