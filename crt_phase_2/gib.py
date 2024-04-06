class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def insert(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left=insert(root.left,key)
    elif key >=root.data:
        root.right=insert(root.right,key)
    return root

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)


root=Node(1)
root=insert(root,2)
root=insert(root,3)
root=insert(root,4)
root=insert(root,5)
inorder_traversal(root) 


# a tree is called as self balanced tree or a balanced tree is the absolute diff between the left height and the right height should be >=1