def draw_grid(x, y):
    grid = ""

    grid += "+---" * x + "+\n"

    for i in range(y):
        grid += "|   " * x + "|\n"
        grid += "+---" * x + "+\n"

    grid = grid[:-1]

    print(grid)
    return grid


def draw_grid_test():
    assert draw_grid(3,4) == '''+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+'''
    assert draw_grid(1,1) == '''+---+
|   |
+---+'''
    assert draw_grid(4,2) == '''+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+'''
    print("tests passed")

if __name__ == "__main__":
    draw_grid_test()
