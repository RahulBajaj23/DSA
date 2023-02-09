class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        Node = self.head
        while Node:
            yield Node
            Node = Node.next

    def insert(self, value, position):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if position == 0:
                newnode.next = self.head
                self.head = newnode
            elif position == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < position - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode


singlylinklist = Slinkedlist()
singlylinklist.insert(8, 1)
singlylinklist.insert(3, 1)
singlylinklist.insert(0, 0)
singlylinklist.insert(4, 1)
print([node.value for node in singlylinklist])
