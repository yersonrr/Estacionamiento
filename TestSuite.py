import unittest
from taller3ver2 import Estacionamiento

class TestSuite(unittest.TestCase):
    def testASimple(self):
        e = Estacionamiento(10)
        self.assertEqual(e.Reservar(800, 1000), True);

    def testSimple2(self):
        e = Estacionamiento(10)
        self.assertEqual(e.Reservar(800, 1000), True);
        self.assertEqual(e.Reservar(1000,1200), True);
        self.assertEqual(e.Reservar(900,1100),  True);
        self.assertEqual(e.Reservar(1700,1800), True);

    def testError(self):
        e = Estacionamiento(10)
        self.assertEqual(e.Reservar(1100, 1000), False);
        self.assertEqual(e.Reservar(1000,1200), True);
        self.assertEqual(e.Reservar(900,1100), True);
        self.assertEqual(e.Reservar(1700,1800), True);
        self.assertEqual(e.Reservar(1000,1200), True);
        self.assertEqual(e.Reservar(900,1100), True);
        self.assertEqual(e.Reservar(1700,1800), True);
        self.assertEqual(e.Reservar(1000,1200), True);
        self.assertEqual(e.Reservar(900,1100), True);
        self.assertEqual(e.Reservar(1700,1800), True);
        self.assertEqual(e.Reservar(1000,1200), True);
        self.assertEqual(e.Reservar(900,1100), True);
        self.assertEqual(e.Reservar(1700,1800), True);
        self.assertEqual(e.Reservar(600,1800), True);
        self.assertEqual(e.Reservar(700,1300), True);
        self.assertEqual(e.Reservar(700,1800), False);
        self.assertEqual(e.Reservar(500,600), False);

    def testFalse(self):
        e = Estacionamiento(10)
        self.assertEqual(e.Reservar(1700,2000), False);
        self.assertEqual(e.Reservar(500,600), False);
        self.assertEqual(e.Reservar(5000,1800), False);
        self.assertEqual(e.Reservar(100,200), False);


if __name__ == '__main__':
    unittest.main()