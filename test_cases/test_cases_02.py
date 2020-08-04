import unittest

class TestNumpy(unittest.TestCase):
    def test_create_99_array(self):
        np.testing.assert_almost_equal(create_99_array(), np.array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9],
           [ 2,  4,  6,  8, 10, 12, 14, 16, 18],
           [ 3,  6,  9, 12, 15, 18, 21, 24, 27],
           [ 4,  8, 12, 16, 20, 24, 28, 32, 36],
           [ 5, 10, 15, 20, 25, 30, 35, 40, 45],
           [ 6, 12, 18, 24, 30, 36, 42, 48, 54],
           [ 7, 14, 21, 28, 35, 42, 49, 56, 63],
           [ 8, 16, 24, 32, 40, 48, 56, 64, 72],
           [ 9, 18, 27, 36, 45, 54, 63, 72, 81]]))
    def test_var(self):
        self.assertAlmostEqual(var(np.arange(10)), 8.25)
        self.assertAlmostEqual(var(np.arange(100)), 833.25)
    def test_std(self):
        self.assertAlmostEqual(std(np.arange(10)), 2.8722813232690143)
        self.assertAlmostEqual(std(np.arange(10), 1), 3.0276503540974917)
        self.assertRaises(ValueError, std, np.arange(1))
    def test_cov(self):
        np.random.seed(123)
        x = np.random.randint(0, 50, 10)
        y = np.random.randint(0, 50, 10)
        self.assertAlmostEqual(cov(x, y), -54.7)
    def test_corr(self):
        np.random.seed(123)
        x = np.random.randint(0, 50, 10)
        y = np.random.randint(0, 50, 10)
        self.assertAlmostEqual(corr(x, y), -0.3409853364175933)

suite = unittest.TestLoader().loadTestsFromTestCase(TestNumpy)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)