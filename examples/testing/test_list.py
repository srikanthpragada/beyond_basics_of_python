import unittest


class TestList(unittest.TestCase):
    def test_len(self):
        self.assertTrue(len([]) == 0)

    def test_append(self):
        l1 = [1, 2]
        l1.append(3)
        self.assertListEqual(l1, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
