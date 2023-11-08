# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:22:27 2023

@author: SOHAIL MUHAMMAD
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def head_node(self):
        return self.head
        

    def find_last_node(self):
        if not self.head:
            return None

        current = self.head
        while current.next:
            current = current.next

        return current

# Create a linked list
my_linked_list = LinkedList()
print('the list is empty')
print(my_linked_list.empty())
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

# Access the head node
head_node = my_linked_list.head_node()

if head_node:
    print(f"The head node contains data: {head_node.data}")
else:
    print("The list is empty.")


# Find the last node
last_node = my_linked_list.head_node()
if last_node:
    print(f"The last node contains data: {last_node.data}")
else:
    print("The list is empty.")
