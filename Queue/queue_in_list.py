class Queue:
    def __init__(self):
        self.list=[]

    def __str__(self):

        values=[str(x) for x in self.list]
        return ' '.join(values)
    def IsEmpty(self):
        if self.list is None:
            return True
        return False

    # push
    def Enqueue(self,value):
        self.list.append(value)

    def Dequeue(self):
        if self.list==[]:
            return"already empty"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.list==[]:
            return"empty"
        else:
            return self.list[0]




que=Queue()
que.Enqueue(1)
que.Enqueue(2)
que.Enqueue(3)
print(que)
# print(que.Dequeue())
print(que.peek())

