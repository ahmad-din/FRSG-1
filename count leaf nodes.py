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
        if node:
            self.display(node.left)
            print(node.data, end=" ")
            self.display(node.right)
    def count_terminals(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_terminals(node.left) + self.count_terminals(node.right)
    
    def delete_terminals(self, node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return None  
     
    
data = [2,3,4,5,1,6,7,8,4,9,2]            
obj = Tree()
root = obj.create_node(8)
root = None  # Initialize the root as None
print('root')
print(root)
# Insert data from the list into the tree
for value in data:
    root = obj.insert(root, value)
print('terminal')   
print(obj.count_terminals(root))
#terminal_count = obj.count_terminals(root)
#print(f"Number of terminal nodes in the tree: {terminal_count}")
print('display')
print(obj.display(root))

# Delete all terminal nodes in the tree
root = obj.delete_terminals(root)

# Display the tree after deleting terminal nodes
print("\nTree after deleting terminal nodes:")
print(obj.display(root))