__author__ = 'yash'
 
import unittest

class Testing(unittest.TestCase):
    def test_boolean(self):
        a = True
        self.assertTrue(a)

if __name__ == '__main__':
    unittest.main()
