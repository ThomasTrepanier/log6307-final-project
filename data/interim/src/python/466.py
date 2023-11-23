# Basic Node class for trees
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# If needed, specialized Node classes for certain trees
class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.balance_factor = 0

class RBNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.color = 'red' # or 'black'

# Your strategy classes would then use these Node classes:

class BSTStrategy(Strategy):
    def buildTree(self, data):
        # Here you'd use the basic Node class for BST logic
        root = Node(data[0]) 
        # ... continue building the BST

class AVLStrategy(Strategy):
    def buildTree(self, data):
        # Here you'd use the AVLNode class for AVL logic
        root = AVLNode(data[0])
        # ... continue building the AVL tree

class RBStrategy(Strategy):
    def buildTree(self, data):
        # Here you'd use the RBNode class for Red-Black logic
        root = RBNode(data[0])
        # ... continue building the Red-Black tree
