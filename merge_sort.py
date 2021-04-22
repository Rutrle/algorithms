def merge_sort(u_list):
    """
    Sorts list in ascending order
    Return a new sorted list

    Divide: Find a midpoint of list and divide into sublists
    Conquer: Recursively sort created sublists
    Combine: Merge the sorted sublists 

    takes O(n log n) time
    """
    if len(u_list) <= 1:
        return u_list

    left_half, right_half = split(u_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(u_list):
    """
    divides unsorted list into sublists
    returns two sublists - left and right
    takes O(log n) time
    """
    midpoint = len(u_list)//2
    left = u_list[:midpoint]
    right = u_list[midpoint:]

    return left, right


def merge(left, right):
    """
    merges two lists or arrays, sorting them in the process
    returns a new merged list
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i = i+1
        else:
            l.append(right[j])
            j = j+1

    while i < len(left):
        l.append(left[i])
        i = i+1

    while j < len(right):
        l.append(right[j])
        j = j+1

    return l


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]

l = merge_sort(alist)
print(l)


def verify_sorted(i_list):
    n = len(i_list)

    if n in [0, 1]:
        return True

    return i_list[0] < i_list[1] and verify_sorted(i_list[1:])


print(verify_sorted(alist))
print(verify_sorted(l))
