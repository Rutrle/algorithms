
def binary_search(searched, searched_list):
    def binary_search_inside(searched, searched_list, left, right):
        middle = (left+right)//2

        if searched_list[middle] == searched:
            return middle
        elif searched_list[middle] > searched:
            return binary_search_inside(searched, searched_list, left, middle-1)
        elif searched_list[middle] < searched:
            return binary_search_inside(searched, searched_list, middle+1, right)

    return binary_search_inside(searched, searched_list, 0, len(searched_list)-1)


my_list = [-1, 0, 4, 10, 20, 50]

print(binary_search(20, my_list))
