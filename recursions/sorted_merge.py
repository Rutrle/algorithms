from linked_list import LinkedList


def sorted_merge(node_A, node_B):
    if node_A == None:
        return node_B
    if node_B == None:
        return node_A

    if node_A.data < node_B.data:
        node_A.next = sorted_merge(node_A.next, node_B)
        return node_A
    else:
        node_B.next = sorted_merge(node_A, node_B.next)
        return node_B


my_list_A = LinkedList([1, 4, 8, 9, 15, 24])

my_list_B = LinkedList([-4, 2, 3, 20])
merged = LinkedList()
merged.head = sorted_merge(my_list_A.head, my_list_B.head)
print(merged)
