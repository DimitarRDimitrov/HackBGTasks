import unittest

from group_by import group_by


class TestGroupBy(unittest.TestCase):

    def test_example1(self):
        self.assertEqual({0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}, group_by(
            lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_example2(self):
        self.assertEqual({'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}, group_by(
            lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))

    def test_example3(self):
        self.assertEqual({0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}, group_by(
            lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_example_zero(self):
        self.assertEqual({}, group_by(lambda x: x % 2, []))

if __name__ == '__main__':
    unittest.main()