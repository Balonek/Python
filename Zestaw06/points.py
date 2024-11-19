import math
import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)
    
    def __repr__(self):      # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other): # obsługa point1 == point2
        if not isinstance(other, Point):
            return False  
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other):        # obsługa point1 != point2
        return not (self == other)

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points
    
class TestPoint(unittest.TestCase): 
    def test_str(self):
        point_1 = Point(1,1)
        point_2 = Point(-1312310,-120231)
        point_3 = Point(0,0)

        self.assertEqual(point_1.__str__(), "(1, 1)")
        self.assertEqual(point_2.__str__(), "(-1312310, -120231)")
        self.assertEqual(str(point_2), "(-1312310, -120231)")
        self.assertEqual(str(point_3), "(0, 0)")


    def test_repr(self):
        point_1 = Point(15,300)
        point_2 = Point(-15000,3000000000)

        self.assertEqual(point_1.__repr__(), "Point(15, 300)")
        self.assertEqual(point_2.__repr__(), "Point(-15000, 3000000000)")
        self.assertEqual(repr(point_1), "Point(15, 300)")
        self.assertEqual(repr(point_2), "Point(-15000, 3000000000)")

    def test_eq(self):
        point_1 = Point(10,10)
        point_2 = Point(-2,-1)
        point_3 = Point(-312312321321,-312312321321)
        point_4 = Point(6946820692,-51341592519)
        point_5 = Point(0,-214913491234)
        point_6 = (23230001,23230001)
        point_7 = Point(-312312321321,-312312321321)
        point_8 = Point(0,-214913491234)

        self.assertFalse(point_1.__eq__(point_2))
        self.assertFalse(point_1.__eq__(point_3))
        self.assertTrue(point_3.__eq__(point_7))
        self.assertTrue(point_5.__eq__(point_8))
        self.assertFalse(point_4 == point_6)
        self.assertFalse(point_2 == point_7)

    def test_ne(self):

        point_1 = Point(3,4)
        point_2 = Point(5,6)
        point_3 = Point(7,8)
        point_4 = Point(5,6)
        point_5 = Point(-3,-4)
        point_6 = Point(-3,-4)

        self.assertTrue(point_2.__ne__(point_3))
        self.assertFalse(point_4.__ne__(point_4))
        self.assertFalse(point_2.__ne__(point_4))
        self.assertTrue(point_1 != point_3)
        self.assertTrue(point_2 != (point_3))
        self.assertFalse(point_5 != point_6)

    def test_add(self):
        point_1 = Point(2,3)
        point_2 = Point(4,5)
        point_3 = Point(-1,-1)
        point_4 = Point(10.5,20.5)
        point_5 = Point(3.14,2.71)
        point_6 = Point(0,0)

        self.assertEqual(point_1.__add__(point_2), Point(6,8))
        self.assertEqual(point_3.__add__(point_1), Point(1,2))
        self.assertEqual(point_4.__add__(point_5), Point(13.64,23.21))
        self.assertEqual(point_4 + point_1, Point(12.5,23.5))
        self.assertEqual(point_1 + point_2, Point(6,8))
        self.assertEqual(point_6 + point_6, Point(0,0))

    def test_sub(self):
        point_1 = Point(10,20)
        point_2 = Point(3,4)
        point_3 = Point(-5,-5)
        point_4 = Point(7,2)
        point_5 = Point(0,0)
            
        self.assertEqual(point_1.__sub__(point_2), Point(7,16))
        self.assertEqual(point_3.__sub__(point_1), Point(-15,-25))
        self.assertEqual(point_4.__sub__(point_2), Point(4,-2))
        self.assertNotEqual(point_2 - point_1, Point(3,4))
        self.assertEqual(point_1 - point_3, Point(15, 25))
        self.assertEqual(point_5 - point_5, Point(0,0))


    def test_mul(self): #self.x * other.x + self.y * other.y
        point_1 = Point(2,10)
        point_2 = Point(-2,3)
        point_3 = Point(2.5, -2.25)
        point_4 = Point(0,-1)

        self.assertEqual(point_1.__mul__(point_2),26)
        self.assertEqual(point_3.__mul__(point_4),2.25)
        self.assertEqual(point_1 * point_4,-10)
        self.assertEqual(point_4 * point_1,-10)

    def test_cross(self): # self.x * other.y - self.y * other.x
        point_1 = Point(7,-3)
        point_2 = Point(2.2,4)
        point_3 = Point(-2.1,520.2)

        self.assertEqual(point_1.cross(point_2),34.6)
        self.assertAlmostEqual(point_3.cross(point_2), -1152.8400000000004, places=5)

    def test_length(self):

        point_1 = Point(41, 238)
        point_2 = Point(17, -54)
        point_3 = Point(-2, 0)
        self.assertAlmostEqual(point_1.length(), 241.50569351466643, places=5)
        self.assertAlmostEqual(point_2.length(), 56.61271941887264, 5)
        self.assertEqual(point_3.length(), 2)


if __name__ == '__main__':
    unittest.main()