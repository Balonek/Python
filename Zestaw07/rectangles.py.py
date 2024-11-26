from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2): 
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Wartosci niepoprawne")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):        # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(self.pt1, self.pt2)
    
    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return  f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
    
    def __eq__(self, other):    # obsługa rect1 == rect2
        if not isinstance(other, Rectangle):
            raise ValueError("Error")
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

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)  
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x) 
        y2 = min(self.pt2.y, other.pt2.y)  
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Wartosci niepoprawne")
        return Rectangle(x1, y1, x2, y2)
    
    def cover(self, other): # prostąkąt nakrywający oba

        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
    
        return Rectangle(x1, y1, x2, y2)

    def make4(self): # zwraca krotkę czterech mniejszych
        center = self.center()
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),
        )
        
import unittest

class TestRectangle(unittest.TestCase): 

    def setUp(self) -> None:
        self.Rectangle1 = Rectangle(2,3,8,7)
        self.Rectangle2 = Rectangle(2,1,3.75,2.5)
        self.Rectangle3 = Rectangle(0.5,2,1,3.5)
        self.Rectangle4 = Rectangle(-50,-2,2,2)
        self.Rectangle5 = Rectangle(2,2,6,6)
        self.Rectangle6 = Rectangle(4,4,8,8)

    def test_str(self):
        self.assertEqual(str(self.Rectangle1), "[(2, 3), (8, 7)]")
        self.assertEqual(str(self.Rectangle2), "[(2, 1), (3.75, 2.5)]")
        self.assertEqual(str(self.Rectangle4), "[(-50, -2), (2, 2)]")

    def test_repr(self):
        self.assertEqual(repr(self.Rectangle1), "Rectangle(2, 3, 8, 7)")

    def test_eq(self):
        self.assertFalse(self.Rectangle3 == self.Rectangle2)
        self.assertFalse(self.Rectangle3 == self.Rectangle4)
        self.assertTrue(self.Rectangle1 == self.Rectangle1)

    def test_ne(self):
        self.assertTrue(self.Rectangle3 != self.Rectangle1)
        self.assertTrue(self.Rectangle2 != self.Rectangle3)
        self.assertFalse(self.Rectangle2 != self.Rectangle2)

    def test_center(self):
        self.assertEqual(self.Rectangle1.center(), Point(5.0, 5.0))
        self.assertEqual(self.Rectangle2.center(), Point(2.875, 1.75))
        self.assertEqual(self.Rectangle4.center(), Point(-24.0, 0.0))

    def test_area(self):
        self.assertEqual(self.Rectangle1.area(), 24)
        self.assertEqual(self.Rectangle2.area(), 2.625)

    def test_move(self):
        self.Rectangle1.move(4, 4)
        self.Rectangle2.move(0, 0)
        self.Rectangle3.move(-10, -2)
        self.assertEqual(self.Rectangle1, Rectangle(6, 7, 12, 11))
        self.assertEqual(self.Rectangle2, Rectangle(2, 1, 3.75, 2.5))
        self.assertEqual(self.Rectangle3, Rectangle(-9.5, 0, -9, 1.5))

    def test_intersection(self):
        self.assertEqual(self.Rectangle5.intersection(self.Rectangle6), Rectangle(4, 4, 6, 6))
        with self.assertRaises(ValueError): self.Rectangle1.intersection(self.Rectangle2)
        with self.assertRaises(ValueError): self.Rectangle2.intersection(self.Rectangle3)

    def test_make4(self):
        self.assertEqual(self.Rectangle2.make4(), (
            Rectangle(2, 1, 2.875, 1.75),
            Rectangle(2.875, 1, 3.75, 1.75),
            Rectangle(2, 1.75, 2.875, 2.5),
            Rectangle(2.875, 1.75, 3.75, 2.5)
        ))

if __name__ == "__main__":
    unittest.main()