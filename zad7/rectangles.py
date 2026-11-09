from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2:
            raise ValueError("box can't have negative width")
        if y1 >= y2:
            raise ValueError("box can't have negative height")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):  # obsługa rect1 == rect2
        Rectangle._is_rectangle(other)
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        Rectangle._is_rectangle(other)
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt2.x + self.pt1.x) / 2, (self.pt2.y + self.pt1.y) / 2)

    def area(self):  # pole powierzchni
        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y
        return width * height

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

    def intersection(self, other):  # część wspólna prostokątów
        Rectangle._is_rectangle(other)
        range_x = [max(self.pt1.x, other.pt1.x), min(self.pt2.x, other.pt2.x)]
        range_y = [max(self.pt1.y, other.pt1.y), min(self.pt2.y, other.pt2.y)]
        if range_x[1] <= range_x[0] or range_y[1] <= range_y[0]:
            return None

        return Rectangle(range_x[0], range_y[0], range_x[1], range_y[1])

    def cover(self, other):  # prostąkąt nakrywający oba
        Rectangle._is_rectangle(other)
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):  # zwraca krotkę czterech mniejszych
        center = self.center()
        r1 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r2 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        r3 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r4 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        return (r1, r2, r3, r4)
        # A-------B   po podziale  A---+---B
        # |       |                |r1 |r2 |
        # |       |                +---+---+
        # |       |                |r3 |r4 |
        # D-------C                D---+---C

    @staticmethod
    def _is_rectangle(obj):
        if not isinstance(obj, Rectangle):
            raise ValueError(f"Expected Rectangle type got {type(obj).__name__}")


# Kod testujący moduł.

import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rect1235 = Rectangle(1, 2, 3, 5)
        self.rect_negative = Rectangle(-1, -2, 3, 5)
        self.rect1155 = Rectangle(1,1,5,5)
        self.rect1133 = Rectangle(1,1,3,3)
        self.rect3355 = Rectangle(3,3,5,5)
        self.rect1335 = Rectangle(1,3,3,5)
        self.rect3153 = Rectangle(3,1,5,3)
        self.rect2244 = Rectangle(2,2,4,4)


    def test_init(self):
        self.assertRaises(ValueError, lambda: Rectangle(3, 4, 2, 7))
        self.assertRaises(ValueError, lambda: Rectangle(3, 4, 5, 3))
        self.assertRaises(ValueError, lambda: Rectangle(3, 4, 2, 3))

    def test_str(self):
        self.assertEqual(str(self.rect1235), "[(1, 2), (3, 5)]")
        self.assertEqual(str(self.rect_negative), "[(-1, -2), (3, 5)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1235), "Rectangle(1, 2, 3, 5)")
        self.assertEqual(repr(self.rect_negative), "Rectangle(-1, -2, 3, 5)")

    def test_eq(self):
        self.assertTrue(self.rect1235 == Rectangle(1, 2, 3, 5))
        self.assertFalse(self.rect1235 == Rectangle(1, 2, 3, 6))
        self.assertFalse(self.rect1235 == Rectangle(1, 2, 2, 5))

    def test_ne(self):
        self.assertFalse(self.rect1235 != Rectangle(1, 2, 3, 5))
        self.assertTrue(self.rect1235 != Rectangle(1, 2, 3, 6))
        self.assertTrue(self.rect1235 != Rectangle(1, 2, 2, 5))

    def test_center(self):
        self.assertEqual(self.rect1235.center(), Point(2, 3.5))
        self.assertEqual(self.rect_negative.center(), Point(1, 1.5))

    def test_area(self):
        self.assertEqual(self.rect1235.area(), 6)
        self.assertEqual(self.rect_negative.area(), 28)

    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 3, 5).move(1, 0), Rectangle(2, 2, 4, 5))
        self.assertEqual(Rectangle(1, 2, 3, 5).move(0, 1), Rectangle(1, 3, 3, 6))

    def test_intersection(self):
        self.assertEqual(self.rect1235.intersection(self.rect1335), Rectangle(1,3,3,5)) 
        self.assertEqual(self.rect1235.intersection(self.rect3153), None)
        self.assertEqual(self.rect3153.intersection(self.rect2244), Rectangle(3,2,4,3))

    def test_cover(self):
        self.assertEqual(self.rect1133.cover(self.rect3355), self.rect1155)
        self.assertEqual(self.rect3355.cover(self.rect1133), self.rect1155)
        self.assertEqual(self.rect3355.cover(self.rect3355), self.rect3355)

    def test_make4(self):
        self.assertEqual(self.rect1155.make4(),(self.rect1335, self.rect3355, self.rect1133, self.rect3153))

    def test_is_rectangle(self):
        self.assertRaises(ValueError, lambda: Rectangle._is_rectangle(4))
        self.assertRaises(
            ValueError, lambda: Rectangle._is_rectangle("Rectangle(2, 3, 4, 5)")
        )
        self.assertRaises(
            ValueError, lambda: Rectangle._is_rectangle("[(2, 3), (4, 5)]")
        )
        self.assertIsNone(Rectangle._is_rectangle(self.rect1235))


if __name__ == "__main__":
    unittest.main()
