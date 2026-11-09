from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):  # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):  # obsługa point1 == point2
        Point._is_point(other)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        Point._is_point(other)
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        Point._is_point(other)
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        Point._is_point(other)
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        Point._is_point(other)
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        Point._is_point(other)
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points

    @staticmethod
    def _is_point(obj):
        if not isinstance(obj, Point):
            raise TypeError(f"Expected Point type got {type(obj).__name__}")


# Kod testujący moduł.

import unittest


class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.zero = Point(0, 0)
        self.up = Point(0, 1)
        self.down = Point(0, -1)
        self.left = Point(-1, 0)
        self.right = Point(1, 0)

    def test_str(self):
        self.assertEqual(str(self.zero), "(0, 0)")
        self.assertEqual(str(self.up), "(0, 1)")
        self.assertEqual(str(self.left), "(-1, 0)")
        self.assertEqual(str(self.right), "(1, 0)")
        self.assertEqual(str(Point(4, 9)), "(4, 9)")

    def test_repr(self):
        self.assertEqual(repr(self.zero), "Point(0, 0)")
        self.assertEqual(repr(self.up), "Point(0, 1)")
        self.assertEqual(repr(self.left), "Point(-1, 0)")
        self.assertEqual(repr(self.right), "Point(1, 0)")
        self.assertEqual(repr(Point(4, 9)), "Point(4, 9)")

    def test_eq(self):
        self.assertTrue(self.zero == self.zero)
        self.assertFalse(self.up == self.right)
        self.assertTrue(self.down == self.down)

    def test_ne(self):
        self.assertFalse(self.zero != self.zero)
        self.assertTrue(self.up != self.right)
        self.assertFalse(self.down != self.down)

    def test_add(self):
        self.assertEqual(self.zero + self.up, self.up)
        self.assertEqual(self.down + self.up, self.zero)
        self.assertEqual(self.right + self.up, Point(1, 1))
        self.assertEqual(Point(6, 3) + Point(-2, 1), Point(4, 4))

    def test_sub(self):
        self.assertEqual(self.zero - self.up, self.down)
        self.assertEqual(self.down - self.up, Point(0, -2))
        self.assertEqual(self.right - self.up, Point(1, -1))
        self.assertEqual(Point(6, 3) - Point(-2, 1), Point(8, 2))

    def test_mul(self):
        self.assertEqual(self.up * self.right, 0)
        self.assertEqual(self.up * Point(4, 4), 4)
        self.assertEqual(self.left * Point(4, 4), -4)
        self.assertEqual(Point(3, 2) * Point(4, 5), 22)

    def test_cross(self):
        self.assertEqual(self.up.cross(self.right), -1)
        self.assertEqual(self.up.cross(Point(4, 4)), -4)
        self.assertEqual(self.left.cross(Point(4, 4)), -4)
        self.assertEqual(Point(3, 2).cross(Point(4, 5)), 7)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertEqual(Point(-3, 4).length(), 5)
        self.assertEqual(Point(-3, -4).length(), 5)
        self.assertEqual(Point(3, -4).length(), 5)
        self.assertEqual(Point(2, 3).length(), sqrt(13))

    def test_is_point(self):
        self.assertRaises(TypeError, lambda: Point._is_point(4))
        self.assertRaises(TypeError, lambda: Point._is_point("Point(2,3)"))
        self.assertRaises(TypeError, lambda: Point._is_point("(2,3)"))
        self.assertIsNone(Point._is_point(Point(3, 4)))


if __name__ == "__main__":
    unittest.main()
