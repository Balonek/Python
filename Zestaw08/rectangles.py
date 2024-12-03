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
    
    @property
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
        return Rectangle(x1, y1, x2, y2)
    
    def cover(self, other): # prostąkąt nakrywający oba

        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
    
        return Rectangle(x1, y1, x2, y2)

    def make4(self): # zwraca krotkę czterech mniejszych
        center = self.center
        return (
            Rectangle(self.pt1.x, self.pt1.y, center.x, center.y),
            Rectangle(center.x, self.pt1.y, self.pt2.x, center.y),
            Rectangle(self.pt1.x, center.y, center.x, self.pt2.y),
            Rectangle(center.x, center.y, self.pt2.x, self.pt2.y),
        )
    def from_points(points):
        if isinstance(points, tuple):
            points = list(points)

        if not isinstance(points, list) or len(points) != 2:
            raise ValueError("Error")
    
        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)
    
    @property
    def top(self):
        return max([self.pt1.y, self.pt2.y])

    @property
    def bottom(self):
        return min([self.pt1.y, self.pt2.y])

    @property
    def left(self):
        return min([self.pt1.x, self.pt2.x])

    @property
    def right(self):
        return max([self.pt1.x, self.pt2.x])
    
    @property
    def width(self):
        return self.right - self.left
    
    @property
    def heigh(self):
        return self.top - self.bottom
    
    @property
    def topleft(self):
        return Point(self.left, self.top)
    
    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)
    
    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)   
    
