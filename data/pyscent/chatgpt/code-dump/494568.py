def test_Zero_One_Knapsack():
    test_cases = [
        ((5, [2, 3, 4], [3, 4, 5]), 7),
        ((7, [2, 3, 3, 4], [3, 4, 5, 6]), 11),
        # ... other test cases ...
    ]
    
    for i, (args, expected) in enumerate(test_cases):
        result = Zero_One_Knapsack(*args)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed")

test_Zero_One_Knapsack()
