class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.leaf = data

def inOrder(arg):
    if arg == root:
        inOrder(arg.left)
        print(arg.leaf)
        inOrder(arg.right)
    else:
        print("tree doesn't exit")

def preOrder(arg):
    if arg == 'root':
        print(arg.leaf)
        preOrder(arg.left)
        preOrder(arg.right)
    else:
        print("tree doesn't exit")

def postOrder(arg):
    if arg == 'root':
        postOrder(arg.left)
        postOrder(arg.right)
        print(arg.leaf)
    else:
        print("tree doesn't exit")

