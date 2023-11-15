# test zero
import unittest

from iters_and_generators_exercise.possible_permutations import possible_permutations


class Tests(unittest.TestCase):
    def test_zero(self):
        result = possible_permutations([1, 2, 3])
        self.assertEqual(next(result), [1, 2, 3])
        self.assertEqual(next(result), [1, 3, 2])
        self.assertEqual(next(result), [2, 1, 3])
        self.assertEqual(next(result), [2, 3, 1])
        self.assertEqual(next(result), [3, 1, 2])
        self.assertEqual(next(result), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()