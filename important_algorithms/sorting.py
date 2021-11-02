def bubble_sort(array):
    '''
    takes O(n**2) time
    :param array: list
    '''
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                not_sorted = True
    return array


def insertion_sort(array):
    '''
    takes O(n**2) time
    :param array: list
    '''
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            j = i-1
            while j >= 1:
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                    j = j-1
                else:
                    break

    return array


def selection_sort(array):
    '''
    takes O(n**2) time
    :param array: list
    '''
    for i in range(len(array)):
        minimum = i
        for j in range(i, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]

    return array


def merge_sort(array):
    '''
    takes O(n logn) time
    :param array: list
    '''

    if len(array) <= 1:
        return array

    middle = len(array)//2

    left, right = merge_sort(array[:middle]),  merge_sort(array[middle:])

    i = 0
    j = 0
    sorted_array = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i = i+1
        else:
            sorted_array.append(right[j])
            j = j+1

    while i < len(left):
        sorted_array.append(left[i])
        i = i+1

    while j < len(right):
        sorted_array.append(right[j])
        j = j+1

    return sorted_array


unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(bubble_sort(unsorted_list))

unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(insertion_sort(unsorted_list))

unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(selection_sort(unsorted_list))

unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(merge_sort(unsorted_list))
