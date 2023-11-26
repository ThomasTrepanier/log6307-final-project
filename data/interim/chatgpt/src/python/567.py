def test_repeated_weights(self):
    W = 7
    wt = [2, 3, 3, 4]
    vals = [3, 4, 5, 6]
    expected_output = 12
    self.assertEqual(Zero_One_Knapsack(len(vals), wt, vals, W), expected_output)
