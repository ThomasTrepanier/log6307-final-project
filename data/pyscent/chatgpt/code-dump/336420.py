def create_unbalanced_tree():
    root = Node(3)
    root.left = Node(1, root)
    root.left.right = Node(2, root.left)

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
