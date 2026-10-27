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

    for i in range(y):
        grid += "|   " * x + "|\n"
        grid += "+---" * x + "+\n"

    grid = grid[:-1]

    print(grid)
    return grid
