class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.leaf = data

def inOrder(root):
    inOrder(root.left)
    print(root.leaf)
    inOrder(root.right)

def preOrder(root):
    print(root.leaf)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    postOrder(root.left)
    postOrder(root.right)
    print(root.leaf)

