import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5), 120)

    def test_roots(self):
        self.assertIs(utils.roots(1,0,1),())

    def test_integrates(self):
        self.assertEqual(utils.integrate('x ** 2 - 1', -1, 1), -4/3)