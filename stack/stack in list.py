# for unlimited size
class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def IsEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    def push(self,value):
        self.list.append(value)
        return "successfull"

    def Pop(self):
        if self.list==[]:
            return "already empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.list==[]:
            return "already empty"
        else:
            return self.list[len(self.list)-1]


st=Stack()
st.push(1)
st.push(3)
st.push(5)


print(st.Pop())

print(st.peek())
print(st)