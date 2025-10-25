# Medium: (5 points)

# 2. Implement a Python function to search for a value in a binary search tree. 
# The method should take the root of the tree and the value to be searched as parameters. 
# It should return True if the value is found in the tree, and False otherwise.

# A Binary Tree Node
class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to insert a new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# print tree inorder
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)

# creating a Tree with root variable "root"
root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


def search_value(root, value):
    while root is not None:
        if root.key > value:
            root = root.left
        elif root.key < value:
            root = root.right
        else:
            print("True")
            return
    print("False")

search_value(root,5)
search_value(root,4)