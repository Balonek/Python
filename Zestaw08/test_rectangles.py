import pytest
from rectangles import Rectangle
from points import Point

class TestRectangle:
    
    @pytest.fixture
    def setup(self) -> None:
        return {
            "Rectangle1": Rectangle(2, 3, 8, 7),
            "Rectangle2": Rectangle(2, 1, 3.75, 2.5),
            "Rectangle3": Rectangle(0.5, 2, 1, 3.5),
            "Rectangle4": Rectangle(-50, -2, 2, 2),
            "Rectangle5": Rectangle(2, 2, 6, 6),
            "Rectangle6": Rectangle(4, 4, 8, 8),
        }

    def test_str(self, setup):
        assert str(setup["Rectangle1"]) == "[(2, 3), (8, 7)]"
        assert str(setup["Rectangle2"]) == "[(2, 1), (3.75, 2.5)]"
        assert str(setup["Rectangle4"]) == "[(-50, -2), (2, 2)]"

    def test_repr(self, setup):
        assert repr(setup["Rectangle1"]) == "Rectangle(2, 3, 8, 7)"

    def test_eq(self, setup):
        assert setup["Rectangle3"] != setup["Rectangle2"]
        assert setup["Rectangle3"] != setup["Rectangle4"]
        assert setup["Rectangle1"] == setup["Rectangle1"]

    def test_ne(self, setup):
        assert setup["Rectangle3"] != setup["Rectangle1"]
        assert setup["Rectangle2"] != setup["Rectangle3"]
        assert setup["Rectangle2"] == setup["Rectangle2"]

    def test_center(self, setup):
        assert setup["Rectangle1"].center == Point(5.0, 5.0)
        assert setup["Rectangle2"].center == Point(2.875, 1.75)
        assert setup["Rectangle4"].center == Point(-24.0, 0.0)

    def test_area(self, setup):
        assert setup["Rectangle1"].area() == 24
        assert setup["Rectangle2"].area() == 2.625

    def test_move(self, setup):
        rect1 = setup["Rectangle1"]
        rect1.move(4, 4)
        assert rect1 == Rectangle(6, 7, 12, 11)

        rect2 = setup["Rectangle2"]
        rect2.move(0, 0)
        assert rect2 == Rectangle(2, 1, 3.75, 2.5)

        rect3 = setup["Rectangle3"]
        rect3.move(-10, -2)
        assert rect3 == Rectangle(-9.5, 0, -9, 1.5)

    def test_intersection(self, setup):
        assert setup["Rectangle5"].intersection(setup["Rectangle6"]) == Rectangle(4, 4, 6, 6)
        with pytest.raises(ValueError):
            setup["Rectangle1"].intersection(setup["Rectangle2"])
        with pytest.raises(ValueError):
            setup["Rectangle2"].intersection(setup["Rectangle3"])

    def test_make4(self, setup):
        rect2 = setup["Rectangle2"]
        sub_rects = rect2.make4()
        assert sub_rects == (
            Rectangle(2, 1, 2.875, 1.75),
            Rectangle(2.875, 1, 3.75, 1.75),
            Rectangle(2, 1.75, 2.875, 2.5),
            Rectangle(2.875, 1.75, 3.75, 2.5),
        )

    def test_from_points(self):
        point1 = Point(1, 1)
        point2 = Point(7, 11)
        point3 = Point(-2,-1)
        point4 = Point(100, 120)

        rect1 = Rectangle.from_points((point1, point2))
        assert rect1 == Rectangle(1, 1, 7, 11)

        rect2 = Rectangle.from_points([point2, point4])
        assert rect2 == Rectangle(7, 11, 100, 120)

        rect3 = Rectangle.from_points([point3, point2])
        assert rect3 == Rectangle(-2, -1, 7, 11)

    def test_top(self, setup):
        assert setup["Rectangle1"].top == 7
        assert setup["Rectangle2"].top == 2.5
        assert setup["Rectangle3"].top == 3.5
        assert setup["Rectangle4"].top == 2

    def test_bottom(self, setup):
        assert setup["Rectangle1"].bottom == 3
        assert setup["Rectangle2"].bottom == 1
        assert setup["Rectangle4"].bottom == -2
        assert setup["Rectangle5"].bottom == 2

    def test_left(self, setup):
        assert setup["Rectangle1"].left == 2
        assert setup["Rectangle2"].left == 2
        assert setup["Rectangle3"].left == 0.5
        assert setup["Rectangle4"].left == -50

    def test_right(self, setup):
        assert setup["Rectangle1"].right == 8
        assert setup["Rectangle2"].right == 3.75
        assert setup["Rectangle3"].right == 1
        assert setup["Rectangle4"].right == 2

    def test_width(self, setup):
        assert setup["Rectangle1"].width == 6
        assert setup["Rectangle2"].width == 1.75
        assert setup["Rectangle4"].width == 52
        assert setup["Rectangle5"].width == 4

    def test_heigh(self, setup):
        assert setup["Rectangle1"].heigh == 4
        assert setup["Rectangle2"].heigh == 1.5
        assert setup["Rectangle3"].heigh == 1.5
        assert setup["Rectangle4"].heigh == 4

    def test_topleft(self, setup):
        assert setup["Rectangle2"].topleft == Point(2, 2.5)
        assert setup["Rectangle3"].topleft == Point(0.5, 3.5)
        assert setup["Rectangle4"].topleft == Point(-50, 2)
        assert setup["Rectangle5"].topleft == Point(2, 6)

    def test_bottomleft(self, setup):
        assert setup["Rectangle1"].bottomleft == Point(2, 3)
        assert setup["Rectangle2"].bottomleft == Point(2, 1)
        assert setup["Rectangle3"].bottomleft == Point(0.5, 2)
        assert setup["Rectangle4"].bottomleft == Point(-50, -2)

    def test_topright(self, setup):
        assert setup["Rectangle4"].topright == Point(2, 2)
        assert setup["Rectangle5"].topright == Point(6, 6)
        assert setup["Rectangle6"].topright == Point(8, 8)

    def test_bottomright(self, setup):
        assert setup["Rectangle1"].bottomright == Point(8, 3)
        assert setup["Rectangle2"].bottomright == Point(3.75, 1)
        assert setup["Rectangle3"].bottomright == Point(1, 2)
