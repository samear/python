"""
https://mail.google.com/mail/u/2/#inbox/FMfcgxwBVzxwtzCJRZdStnBtbJQGHDfm
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)
