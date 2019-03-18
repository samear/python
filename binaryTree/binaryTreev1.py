"""
Binary Tree and its traversal using python.

Binary tree are the tree where one node can have only two child and
cannot have more than two.
Traversal means visiting all the nodes of the Binary tree.
There are three types of traversal - In Order, Pre Order, and Post Order.
https://www.learnsteps.com/binary-tree-traversal-using-python/
"""

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#inOrder traversal: visit left first, then root and then right.
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

#preOrder traversal: visit root first, then left then right
def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

#postOrder traversal: visit left first then right, then root
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)
"""
bulding the tree below:

                2
               / \
             4     5
            / \   / \
           7  10 1   3

root = Node(2)
root.left = Node(4)
root.left.left = Node(7)
root.left.right = Node(10)
root.right = Node(5)
root.right.lef = Node(1)
root.right.right = Node(3)
"""
