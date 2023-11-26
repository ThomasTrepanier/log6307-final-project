def test_overlapping_activities(self):
    activities = [(1, 3), (2, 4), (3, 5), (4, 6)]
    expected_output_1 = [(1, 3), (3, 5)]
    expected_output_2 = [(2, 4), (4, 6)]
    result = greedyActivitySelection(activities)
    self.assertTrue(result == expected_output_1 or result == expected_output_2)
