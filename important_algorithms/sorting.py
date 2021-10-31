def bubble_sort(array):
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                not_sorted = True
    return array


unsorted_list = [2, 5, 4, 1, 8, 44, -5, 6, 7, 2, 4, 55]

print(bubble_sort(unsorted_list))
