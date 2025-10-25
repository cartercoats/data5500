# Easy: (3 points)

# Write a Python function to insert a value into a binary search tree. 
# The function should take the root of the tree and the value to be inserted as parameters.

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

inorder(root)

# insert user genrated value

user_num = int(input("\nPlease type a number to be inserted: "))
root = insert(root, user_num)

inorder(root)