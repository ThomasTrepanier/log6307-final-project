def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key;
    else: return node;
    return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right));
