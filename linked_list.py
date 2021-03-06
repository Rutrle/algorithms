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

    def search(self, key):
        """
        search for the first node containing data matching key
        Return node or if not found, return None
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1), but finding the node takes O(n) time

        therefore overall timeis O(n)
        """
        if index == 0:
            self.add(data)

        elif index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node_obj = current
            next_node_obj = current.next_node

            prev_node_obj.next_node = new
            new.next_node = next_node_obj

    def remove(self, key):
        """
        removes node containing data matching the key, 
        returns the node or if key was not found None,
        this takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:  # current must be a valid node and the key was not found
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

        return current

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


if __name__ == "__main__":
    l = LinkedList()
    N1 = Node(10)
    l.head = N1
    print(l.size())
    l.add(5)
    l.add(105)
    l.add(2)

    print(l.size())
    print(l)
    n = l.search(5)
    print(n)
