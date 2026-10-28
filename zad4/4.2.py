import unittest


def make_ruller(length):
    ruller = ""
    ruller += "|"
    for x in range(length):
        ruller += "....|"

    ruller += "\n"
    ruller += "0"

    for x in range(1, length + 1):
        ruller += f"{x:>5}"

    print(ruller)
    return ruller


def make_grid(x, y):
    grid = ""
    grid += "+---" * x + "+\n"

    for _ in range(y):
        grid += "|   " * x + "|\n"
        grid += "+---" * x + "+\n"

    grid = grid[:-1]

    print(grid)
    return grid


class TestRuller(unittest.TestCase):
    def test_ruller(self):
        expected = "|....|\n0    1"
        self.assertEqual(make_ruller(1), expected)

    def test_ruller_long(self):
        expected = "|....|....|....|....|....|....|....|....|....|....|....|....|\n0    1    2    3    4    5    6    7    8    9   10   11   12"
        self.assertEqual(make_ruller(12), expected)


class TestGrid(unittest.TestCase):
    def test_grid_1(self):
        expected = """+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+"""
        self.assertEqual(make_grid(3, 4), expected)

    def test_grid_2(self):
        expected = """+---+
|   |
+---+"""
        self.assertEqual(make_grid(1, 1), expected)

    def test_grid_3(self):
        expected = """+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+"""
        self.assertEqual(make_grid(4, 2), expected)


if __name__ == "__main__":
    print("---4.2---")
    unittest.main()
