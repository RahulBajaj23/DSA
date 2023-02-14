# for limited size
class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list=[]

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def IsFull(self):
        if len(self.list)==self.maxsize:
            return True
        return False
    def push(self,value):
        if len(self.list)==self.maxsize:
            return "already full"
        else:
            self.list.append(value)
            return "sucessfill"
    def pop(self):
        if self.list==[]:
            return "already empty"
        else:
            return self.list.pop()
    def peek(self):
        if self.list==[]:
            return "already empty"
        else:
            return self.list[len(self.list)-1]

st1=Stack(4)
st1.push(1)
st1.push(2)
st1.push(3)
# print(st1)
print(st1.pop())
# print(st1.peek())
print(st1)