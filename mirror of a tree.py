# -*- coding: utf-8 -*-
"""
Created on Mon Nov 6 12:51:08 2023

@author: SOHAIL MUHAMMAD
"""
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

    def display(self, node):
        if node is not None:
            self.display(node.left)
            print(node.data)
            self.display(node.right)

    def mirror(self, node):
        if node is None:
            return
        else:
            temp = node
            self.mirror(node.left)
            self.mirror(node.right)
            temp = node.left
            node.left = node.right
            node.right = temp

data = [2, 3, 4, 5, 1, 6, 7, 8, 4, 9, 2]
obj = Tree()
root = obj.create_node(8)
root = None  # Initialize the root as None
print('root')
print(root)
# Insert data from the list into the tree
for value in data:
    root = obj.insert(root, value)

print('display')
obj.display(root)

obj.mirror(root)  # Call the mirror method on the root node
print('Mirror display')
obj.display(root)
