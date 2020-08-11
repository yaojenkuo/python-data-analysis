import unittest

class TestPandas102(unittest.TestCase):
    def test_most_counties(self):
        self.assertEqual(most_counties(census_df), 'Texas')
    def test_top_three_states(self):
        self.assertEqual(top_three_states(census_df), ['California', 'Texas', 'Illinois'])
    def test_pop_change_most_county(self):
        self.assertEqual(pop_change_most_county(census_df), 'Harris County')
    def test_filter_counties(self):
        test_df = pd.DataFrame()
        test_df['STNAME'] = ['Iowa', 'Minnesota', 'Pennsylvania', 'Rhode Island', 'Wisconsin']
        test_df['CTYNAME'] = 'Washington County'
        pd.testing.assert_frame_equal(filter_counties(census_df), test_df)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPandas102)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)