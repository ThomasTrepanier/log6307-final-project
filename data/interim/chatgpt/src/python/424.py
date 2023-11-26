class BSTStrategy(Strategy):
    ...
    # This method name should match the abstract method name
    def buildTree(self, data):
        return self.buildBinaryTree(data)

    # Add these missing methods from the Strategy class
    def leftHeight(self):
        return self.left_height()

    def rightHeight(self):
        return self.right_height()

    # Rename this to match the abstract method name
    def visualizeTree(self, tree):
        return self.visualize_tree(tree)

    # Add dummy implementations for the rest of the methods from Strategy
    def rotateLeft(self):
        pass

    def rotateRight(self):
        pass

    def LeftRightRotation(self):
        pass

    def RightLeftRotation(self):
        pass

    def checkForBalance(self):
        pass

    def printBalanceFactors(self):
        pass

    def calculateBalanceFactors(self):
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def findNode(self, value):
        pass

    def findCommonAncestor(self, value1, value2):
        pass
