import unittest

class TestPandas101(unittest.TestCase):
    def test_most_summer_gold_country(self):
        self.assertEqual(most_summer_gold_country(olympic_medal_table), 'United States')
    def test_largest_gold_difference(self):
        self.assertEqual(largest_gold_difference(olympic_medal_table), 'United States')
    def test_largest_ratio(self):
        self.assertEqual(largest_ratio(olympic_medal_table), 'Hungary')

suite = unittest.TestLoader().loadTestsFromTestCase(TestPandas101)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)