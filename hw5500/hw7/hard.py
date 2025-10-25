# Hard: (Essay, 7 points)

# 3. Explain the process of deleting a node from a binary search tree in Python. 
# Discuss how you would handle different cases, such as deleting a node with one, or two children. 
# Additionally, explain any potential challenges or edge cases that may arise during the 
# deletion process and how you would address them.

1. Create a base case for when the node is not in the tree. That's how you'll know it worked
2. Find the node. You'll need to take rights and lefts down the tree'
3. If the node has no children, just delete the node.
4. If the node has one child, the child will take the place of the deleted parent
5. If the node has two children, you will need to find the largest value on the left subtree 
or the smallest value on the right subtree. Copy the successor to the node you want to delete, then delete the successor node.

In odd cases where the tree is empty or the value you're looking for isn't there, the base case should account for that.