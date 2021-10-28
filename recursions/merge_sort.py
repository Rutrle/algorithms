def merge_sort(array):
    if len(array) == 1:
        return array

    middle = len(array)//2

    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(arr1, arr2):
    i = 0
    j = 0
    sorted_arr = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i = i+1
        else:
            sorted_arr.append(arr2[j])
            j = j+1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i = i+1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j = j+1

    return sorted_arr


my_list = [3, 1, 4, 2, -1]

print(merge_sort(my_list))
