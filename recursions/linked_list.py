class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes != None:
            node = Node(nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(item)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


L = [1, 2, 3, 4, 5, 6]
my_LL = LinkedList(L)
print(my_LL)
print(my_LL.head)
print(my_LL.head.next)
print(my_LL.head.next.next)
