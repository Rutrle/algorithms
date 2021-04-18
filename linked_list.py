class Node:
    """
    An object for storing single node of a linked list
    models attributes - data and link to the next node in the list
    """

    data = None
    datas = []
    next_node = None

    def __init__(self, data):
        self.data = data
        self.datas.append(data)

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns number of nodes in the list
        takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)


l = LinkedList()
N1 = Node(10)
l.head = N1
print(l.size())
l.add(5)
print(l.size())
print(l)
