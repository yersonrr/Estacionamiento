import unittest
from taller3 import main

class TestSuite(unittest.TestCase):
    def testASimple(self):
        self.assertEqual(main('test1.txt'), True);

    def testSimple2(self):
        self.assertEqual(main('test3.txt'), True);

    def testError(self):
        self.assertEqual(main('test4.txt'), True);

    def testFalse(self):
        self.assertEqual(main('test2.txt'), False);

if __name__ == '__main__':
    unittest.main()