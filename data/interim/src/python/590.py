def test_all_activities_overlap(self):
    activities = [(1, 5), (2, 4), (3, 6), (4, 7)]
    result = greedyActivitySelection(activities)
    self.assertEqual(len(result), 1)
    self.assertIn(result[0], activities)
