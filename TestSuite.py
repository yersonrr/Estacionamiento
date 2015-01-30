import unittest
from taller3ver2 import *

class TestSuite(unittest.TestCase):
    def testASimple(self):
        e = Estacionamiento(10)
        e.agregarI(800, 1000)
		e.agregarI(1000,1200)
		e.Reservar(900,1100)
		e.Reservar(1700,1800)
		e.Reservar(1000,5000)

if __name__ == '__main__':
    unittest.main()