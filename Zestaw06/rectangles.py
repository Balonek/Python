from points import Point
import unittest
class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2): 
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):        # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)
    
    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return  f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):    # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            return False  
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not (self == other)
    def center(self):           # zwraca środek prostokąta
        point_x = (self.pt1.x + self.pt2.x) / 2
        point_y = (self.pt1.y + self.pt2.y) / 2
        return Point(point_x, point_y)
        
    def area(self):            # pole powierzchni
        return  abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)
    
    def move(self, x, y):       # przesunięcie o (x, y)
        for value in [self.pt1, self.pt2]:
            value.x += x
            value.y += y

class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.Rectangle1 = Rectangle(2,7,8,3)
        self.Rectangle2 = Rectangle(11,2.5,3.75,1)
        self.Rectangle3 = Rectangle(11,2.5,3.75,1)
        self.Rectangle4 = Rectangle(-50,10,2,8)

    def test_str(self):
        self.assertEqual(str(self.Rectangle1), "[(2, 7), (8, 3)]")
        self.assertEqual(str(self.Rectangle2), "[(11, 2.5), (3.75, 1)]")
        self.assertEqual(str(self.Rectangle4), "[(-50, 10), (2, 8)]")

    def test_repr(self):
        self.assertEqual(repr(self.Rectangle1), "Rectangle(2, 7, 8, 3)")

    def test_eq(self):
        self.assertTrue(self.Rectangle3 == self.Rectangle2)
        self.assertFalse(self.Rectangle3 == self.Rectangle4)
        self.assertTrue(self.Rectangle1 == self.Rectangle1)

    def test_ne(self):
        self.assertTrue(self.Rectangle3 != self.Rectangle1)
        self.assertFalse(self.Rectangle2 != self.Rectangle3)
        self.assertFalse(self.Rectangle2 != self.Rectangle2)

    def test_center(self):
        self.assertEqual(self.Rectangle1.center(), Point(5.0,5.0))
        self.assertEqual(self.Rectangle2.center(), Point(7.375,1.75))
        self.assertEqual(self.Rectangle4.center(), Point(-24.0,9.0))

    def test_area(self):

        self.assertEqual(self.Rectangle1.area(), 24)
        self.assertEqual(self.Rectangle2.area(), 10.875)

    def test_move(self):
        self.Rectangle1.move(4,4)
        self.Rectangle2.move(0,0)
        self.Rectangle3.move(-10,-2)
        self.assertEqual(self.Rectangle1, Rectangle( 6,11,12,7))
        self.assertEqual(self.Rectangle2, Rectangle(11,2.5,3.75,1))
        self.assertEqual(self.Rectangle3, Rectangle(1,0.5,-6.25,-1))

if __name__ == "__main__":
    unittest.main()
