class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.leaf = data

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.leaf)
        inOrder(root.right)
    else:
        print("tree doesn't exit")

def preOrder(root):
    if root:
        print(root.leaf)
        preOrder(root.left)
        preOrder(root.right)
    else:
        print("tree doesn't exit")

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.leaf)
    else:
        print("tree doesn't exit")

