import unittest


def issorted(seq):
    for i in range(1, len(seq)):
        if seq[i] < seq[i - 1]:
            return False
    return True


class TestIsSorted(unittest.TestCase):
    def test_list(self):
        self.assertTrue(issorted([1, 2, 3]), "Testing a list")

    def test_tuple(self):
        self.assertFalse(issorted((1, 3, 2)), "Testing a tuple")

    def test_empty(self):
        self.assertTrue(issorted([]), "Testing empty list")

    def test_numbers(self):
        self.assertTrue(issorted(10, 20, 23), "Testing individual numbers")


if __name__ == '__main__':
    unittest.main()
