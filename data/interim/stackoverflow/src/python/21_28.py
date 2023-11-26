def tree_to_tuple(node):
    if isinstance(node, TreeNode):

        if node.left is not None and node.right is not None:
            node_mid = node.key
            node_left = tree_to_tuple(node.left)
            node_right = tree_to_tuple(node.right)

            return (node_left, node_mid, node_right)

        elif node.left is None and node.right is None:
            return node.key

        elif node.left is None and node.right is not None:
            node_mid = node.key
            node_right = tree_to_tuple(node.right)
            node_left = None

            return (node_left, node_mid, node_right)

        elif node.left is not None and node.right is None:
            node_mid = node.key
            node_right = None
            node_left = tree_to_tuple(node.left)

            return (node_left, node_mid, node_right)

    else:
        print("It's not a tree")
