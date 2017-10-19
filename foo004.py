import unittest

class Area:
    def quadrada(self):
        return self.lado1 * self.lado2
    
class MyCalcTest(unittest.TestCase):
    def testAreaQuadrada(self):
        area = Area()
        area.lado1 = 3
        area.lado2 = 9
        
        self.assertEqual(27, area.quadrada())

if __name__ == '__main__':
    unittest.main()