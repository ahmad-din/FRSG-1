# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:05:26 2023

@author: SOHAIL MUHAMMAD
"""

# to print all the ancestors of the node
class Tree_Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create_node(self, data):
        return Tree_Node(data)

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        else:
            print('node already exists in the tree')
        return node

    def travers_Postorder(self, root):
        if root is not None:
            self.travers_Postorder(root.left)
            self.travers_Postorder(root.right)
            print(root.data)
    
    def ancestors(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if (self.ancestors(root.left, key) or self.ancestors(root.right, key)):
            print(root.data, end=' - ')
            return True
        return False

obj = Tree()
data = [2, 3, 4, 5, 1, 6, 7, 8, 4, 9, 2]
root = None  # Initialize the root as None
root = obj.create_node(8)

print('root')
print(root)
# Insert data from the list into the tree
for value in data:
    root = obj.insert(root, value)
obj.travers_Postorder(root)  # Remove the print statement
print(obj.ancestors(root, 4))
