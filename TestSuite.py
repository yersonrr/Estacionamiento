import unittest
from taller3 import main

class TestSuite(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(main('test1.txt'), 'YES');

    def testFalse(self):
        self.assertEqual(main('test2.txt'), 'YES');

if __name__ == '__main__':
    unittest.main()