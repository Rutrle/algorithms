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


n1 = Node(1)
print(Node.data)
n2 = Node(2)
print(Node.data)
n3 = Node(3)
print(Node.data)
print(Node.datas)
