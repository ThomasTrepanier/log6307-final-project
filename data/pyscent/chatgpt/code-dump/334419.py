def create_unbalanced_tree():
    root = Node(1)
    root.right = Node(2, root)
    root.right.right = Node(3, root.right)
    root.right.right.right = Node(4, root.right.right)
    # Continue adding nodes in a right-heavy fashion for more imbalance.

    # Calculate balance factors
    update_balance_factors(root)
    
    return root

def update_balance_factors(node):
    if node is None:
        return 0
    left_height = update_balance_factors(node.left)
    right_height = update_balance_factors(node.right)
    node.balance_factor = left_height - right_height
    return max(left_height, right_height) + 1

# Create the unbalanced tree
root = create_unbalanced_tree()
