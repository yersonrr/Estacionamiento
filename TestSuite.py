import unittest
from taller3ver2 import Estacionamiento

class TestSuite(unittest.TestCase):
    def testASimple(self):
        e = Estacionamiento(10)
        e.agregarI(800, 1000)
        e.Reservar(1000,5000)
        self.assertEqual(main('test1.txt'), True);

    def testSimple2(self):
        e = Estacionamiento(10)
        e.agregarI(800, 1000)
        e.agregarI(1000,1200)
        e.Reservar(900,1100)
        e.Reservar(1700,1800)
        e.Reservar(1000,5000)
        self.assertEqual(main('test3.txt'), True);

    def testError(self):
        e = Estacionamiento(10)
        e.agregarI(800, 1000)
        e.agregarI(1000,1200)
        e.Reservar(900,1100)
        e.Reservar(1700,1800)
        e.Reservar(1000,5000)
        self.assertEqual(main('test4.txt'), True);

    def testFalse(self):
        e = Estacionamiento(10)
        e.agregarI(800, 1000)
        e.agregarI(1000,1200)
        e.Reservar(900,1100)
        e.Reservar(1700,1800)
        e.Reservar(1000,5000)
        self.assertEqual(main('test2.txt'), False);

if __name__ == '__main__':
    unittest.main()