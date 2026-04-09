import unittest


def is_even(n):
    return n % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(2))

    def test_odd_number(self):
        self.assertFalse(is_even(3))

    def test_zero(self):
        self.assertTrue(is_even(0))


if __name__ == '__main__':
    unittest.main()
