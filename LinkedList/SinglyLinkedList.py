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

    # Insert a node in linkedlist
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


    # Traverse singlylinkedlist
    def traversal(self):
        if self.head is None:
            print("singlyLinkedlist is not exist")
        else:
            tempnode=self.head
            while tempnode is not None:
                print(tempnode.value)
                tempnode=tempnode.next

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # search a nodevalue
    def search(self,value):
        if self.head is None:
            print("sll does not exits")
        else:
            tempnode=self.head
            while tempnode is not None:
                if tempnode.value==value:
                    return tempnode.value
                tempnode=tempnode.next
            return "Value not exists"
 
    # delete a node
    def delete(self,position):
        if self.head is None:
            print("LinkedList not exist")
        else:
            if position==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif position==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempnode=self.head
                    while tempnode is not None:
                        if tempnode.next==self.tail:
                            break
                        tempnode=tempnode.next
                    tempnode.next=None
                    self.tail=tempnode
            else:
                tempnode=self.head
                index=0
                while index<position-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next




singlylinklist = Slinkedlist()
singlylinklist.insert(2,3)

singlylinklist.insert(0,0)

singlylinklist.insert(3,1)

singlylinklist.insert(2,2)

singlylinklist.insert(6,1)

singlylinklist.insert(4,5)



print([node.value for node in singlylinklist])

singlylinklist.traversal()
singlylinklist.reverse()
print([node.value for node in singlylinklist])


# print(singlylinklist.search(4))

# singlylinklist.delete(2)
# print([node.value for node in singlylinklist])
