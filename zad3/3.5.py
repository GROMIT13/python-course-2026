def draw_ruller(length):
    ruller = ""

    ruller += "|"
    for x in range (length):
        ruller += "....|"

    ruller += "\n"
    ruller += "0"

    for x in range(1,length + 1):
        ruller += f"{x:>5}"
    
    print(ruller)
    return ruller

def draw_ruller_test():
    assert draw_ruller(12) == '''|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12'''
    assert draw_ruller(1) == '''|....|\n0    1'''
    print("tests passed")

if __name__ == "__main__":
    draw_ruller_test()

