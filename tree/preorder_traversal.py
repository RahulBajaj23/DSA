
class TreeNode:
    def __int__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None


def PreorderTraversal(RootNode):
        if RootNode is None:
            return
        print(RootNode.data,end="->")
        PreorderTraversal(RootNode.leftchild)
        PreorderTraversal(RootNode.rightchild)

def insert(RootNode,newvalue):
    if RootNode is None:
        RootNode=TreeNode(newvalue)
        return RootNode
    if newvalue<RootNode.data:
         RootNode.leftchild=insert(RootNode.leftchild,newvalue)
    else:
         RootNode.rightchild=insert(RootNode.rightchild,newvalue)
    return RootNode

RootNode=insert(None,50)
insert(RootNode,22)
insert(RootNode,42)
insert(RootNode,46)
insert(RootNode,25)
insert(RootNode,17)
insert(RootNode,12)
insert(RootNode,16)
PreorderTraversal(RootNode)


