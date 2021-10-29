from linked_list import LinkedList, Node


def linked_list_reverse(head):

    if head.data == None or head.next == None:
        return head
    node = linked_list_reverse(head.next)
    head.next.next = head
    head.next = None
    print(f"node data: {node.data}")
    return node


k = [1, 2, 3, 4, 5]
my_ll = LinkedList(k)

print(my_ll)
# print(linked_list_reverse(my_ll.head))
new_head = linked_list_reverse(my_ll.head)
print(new_head)

my_ll.head = new_head
print(my_ll)
