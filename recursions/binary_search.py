
def binary_search(searched, list):
    def binary_search_inside(searched, list, left, right):
        middle = (left+right)//2

        if list[middle] == searched:
            return middle
        elif list[middle] > searched:
            return binary_search_inside(searched, list, left, middle-1)
        elif list[middle] < searched:
            return binary_search_inside(searched, list, middle+1, right)

    return binary_search_inside(searched, list, 0, len(list)-1)


list = [-1, 0, 4, 10, 20, 50]

print(binary_search(20, list))
