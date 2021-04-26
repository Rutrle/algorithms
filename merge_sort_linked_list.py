from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - recursively divide the linked list into sublists containing a single node
    - repeatedly merge the sublists to produce sorted sublists until one remains
    runs in O(k n log n)
    """

    if linked_list.size() == 1 or linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    divide the unsorted list at midpoint into sublists
    takes O(k log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

    return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes¨
    Returns a new, merged list
    runs in linear time
    """
    # crate a new linked list containing nodes from merging left and right
    merged = LinkedList()
    # Add a fake head that is discarded later
    merged.add(0)
    # setcurrent to tohe head of the linked list
    current = merged.head

    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    # iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # if the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right  to set loop condition to False
            right_head = right_head.next_node
        # if the head node of right is None, we're past the tail
        # Add the node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left  to set loop condition to False
            left_head = left_head.next_node
        else:
            # not at either tail node
            # #obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                # move left head to the next node
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # move current to next node
        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged


k = LinkedList()
k.add(50)
k.add(5)
k.add(441)
k.add(1)
k.add(3)
k.add(14)
k.add(65)
print(k)
print(merge_sort(k))
