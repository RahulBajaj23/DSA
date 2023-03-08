class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        Node=self.head
        while Node:
            yield Node
            Node=Node.next
class Queue:
    def __init__(self):
        self.LinkedList=LinkedList()

    def __str__(self):
        values=[str(x) for x in self.LinkedList]
        return ' '.join(values)

    def IsEmpty(self):
        if self.LinkedList.head==None:
            return True
        return False

    def Enqueue(self,value):
        newnode=Node(value)
        if self.LinkedList.head==None:
            self.LinkedList.head=newnode
            self.LinkedList.tail=newnode
        else:
            newnode.next=None
            self.LinkedList.tail.next=newnode
            self.LinkedList.tail=newnode
    def Dequeue(self):
        if self.LinkedList.head==None:
            return "Already Empty"
        else:
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            else:
                Nodevalue=self.LinkedList.head
                self.LinkedList.head=self.LinkedList.head.next
                return Nodevalue

    def peek(self):
        if self.LinkedList.head==None:
            return "Already Empty"
        else:
            return self.LinkedList.head





Que=Queue()
Que.Enqueue(2)
Que.Enqueue(4)
Que.Enqueue(6)
print(Que)

print(Que.Dequeue())
print(Que)

print(Que.peek())
