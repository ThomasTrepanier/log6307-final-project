from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def buildTree(self, data):
        pass

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def rotate(self):
        pass

class BSTStrategy(Strategy):
    def buildTree(self, data):
        # implement BST-specific tree building logic
        pass

    def insert(self, value):
        # BST insertion logic
        pass

    def delete(self, value):
        # BST deletion logic
        pass

    def rotate(self):
        # For a basic BST, rotations might not be necessary.
        pass

class AVLStrategy(Strategy):
    def buildTree(self, data):
        # AVL tree-building logic
        pass

    def insert(self, value):
        # AVL insertion logic (might involve rotations)
        pass

    def delete(self, value):
        # AVL deletion logic (might involve rotations)
        pass

    def rotate(self):
        # Implement AVL-specific rotations here
        pass

class RBStrategy(Strategy):
    def buildTree(self, data):
        # Red-Black tree-building logic
        pass

    def insert(self, value):
        # Red-Black insertion logic (might involve color flipping and rotations)
        pass

    def delete(self, value):
        # Red-Black deletion logic (might involve color flipping and rotations)
        pass

    def rotate(self):
        # Implement Red-Black-specific rotations here
        pass

class Tree:
    def __init__(self, strategy):
        self.strategy = strategy

    def buildTree(self, data):
        self.strategy.buildTree(data)

    def insert(self, value):
        self.strategy.insert(value)

    def delete(self, value):
        self.strategy.delete(value)

    def rotate(self):
        self.strategy.rotate()
