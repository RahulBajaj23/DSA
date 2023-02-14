class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        Node = self.head
        while Node:
            yield Node
            Node = Node.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def Isempty(self):
        if self.LinkedList.head==None:
            return True
        return False
    def push(self,value):
        newnode=Node(value)
        newnode.next=self.LinkedList.head
        self.LinkedList.head=newnode
    def pop(self):
        if self.LinkedList.head==None:
             return "already empty"
        else:
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            else:
                nodevalue=self.LinkedList.head.value
                self.LinkedList.head=self.LinkedList.head.next
                return nodevalue
    def peek(self):
        if self.LinkedList.head is None:
            return "Linkedlist not exists"
        else:
            return self.LinkedList.head.value
#           nodevalue=self.LinkedList.head.value
#             return nodevalue


st=Stack()
st.push(2)
# st.push(3)
# st.push(4)
print(st)

print(st.pop())
# print(st.peek())
