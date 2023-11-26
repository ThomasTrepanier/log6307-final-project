def rightRotate(tree, val):
    """Right rotate a subtree
    Args: tree(node): root node of the tree, val(int): value of the node to be rotated
    Returns: root node of the subtree
    """
    node = findNode(tree, val)
    if node is None or node.left is None:
        return tree
    temp = node.left
    node.left = temp.right
    if node.left:  # Update parent pointer for the left child of the rotated node
        node.left.parent = node
    temp.right = node
    if node.parent is not None:
        if node.parent.left == node:
            node.parent.left = temp
        else:
            node.parent.right = temp
    temp.parent = node.parent
    node.parent = temp
    
    # If rotated node was the root, return the new root (temp), otherwise return the original root (tree)
    return temp if temp.parent is None else tree
