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
            print('Node already exists in the tree')
        return node
    def find(self, node, data, depth = 1):
        if node is None:
            return None
        if data < node.data:
            return self.find(node.left, data, depth + 1)
        elif data > node.data:
            return self.find(node.right, data, depth + 1)
        else:
            return depth
    def find_max(node):
        current = root
        while current.right:
            current = current.right
        return current.data
    def find_min(node):
        current = root
        while current.left:
            current = current.left
        return current.data
    
    # def max_depth(self):
    #     if self is None:
    #         return 0
    #     return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
        
            
data = [2,3,4,5,1,6,7,8,4,9,2]
            
obj = Tree()
root = None  # Initialize the root as None
root = obj.create_node(8)


# Insert data from the list into the tree
for value in data:
    root = obj.insert(root, value)

print('max_depth')
obj.max_depth()
    
print('find_max')
print(obj.find_max())


print('fin minimum value')
print(obj.find_min())

req_val = 6


result = obj.find(root, req_val)
if result is not None:
    print(f"Value '{req_val}' is at depth {result} in the tree.")
else:
    print(f"Value '{req_val}' is not found in the tree.")
    
