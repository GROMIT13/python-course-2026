from math import sqrt


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return "({self.x}, {self.y})".format()

    def __repr__(self):         # zwraca string "Point(x, y)"
        return "Point({self.x}, {self.y})".format()

    def __eq__(self, other):    # obsługa point1 == point2
        Point.__is_point(other) 
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):    # obsługa point1 != point2
        Point.__is_point(other) 
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        Point.__is_point(other) 
        return Point(self.x + other.x,self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        Point.__is_point(other) 
        return Point(self.x - other.x,self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        Point.__is_point(other) 
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        Point.__is_point(other) 
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points
    
    @staticmethod
    def __is_point(obj):
        if not isinstance(obj, Point):
            raise TypeError("Expected Point type got {type(obj).__name__}".format())


# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    def setUp(self) -> None:
        self.zero = Point(0,0)
        self.up = Point(0,1)
        self.down = Point(0,-1)
        self.left = Point(-1,0)
        self.right = Point(1,0)

    def test_str(self):
        self.assertEqual()

    def test_repr(self):
        self.assertEqual()

    def test_eq(self):
        self.assertEqual()

    def test_ne(self):
        self.assertEqual()

    def test_add(self):
        self.assertEqual()

    def test_sub(self):
        self.assertEqual()

    def test_mul(self):
        self.assertEqual()

    def test_cross(self):
        self.assertEqual()

    def test_length(self):
        self.assertEqual()

    def test_hash(self):
        self.assertEqual()

    def test_is_point(self):
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()
