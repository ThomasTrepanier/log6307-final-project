class Tree:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def buildBinaryTree(self, data):
        return self.strategy.buildTree(data)
