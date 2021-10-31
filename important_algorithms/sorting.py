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


unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(bubble_sort(unsorted_list))

unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(insertion_sort(unsorted_list))
