from binaryTreev1 import Node
from binaryTreev1 import inOrder
from binaryTreev1 import preOrder
from binaryTreev1 import postOrder

root = Node(2)
root.left = Node(4)
root.left.left = Node(7)
root.left.right = Node(10)

root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(3)

print("inOrder")
inOrder(root)
print("preOrder")
preOrder(root)
print("postOrder")
postOrder(root)
