import unittest

from sort import missing_number


class test_sort(unittest.TestCase):
    def test_find_missing (self):
        self.assertEqual(missing_number([1,2,3,5,6,7,9]),[4,8])
    def test_list(self):
        self.assertEqual(missing_number('welcome'),'invalid input')
if __name__ == '__main__':
    unittest.main()
