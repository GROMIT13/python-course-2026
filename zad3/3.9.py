def exercise_3_9(list):
    out = []
    for element in list:
        out.append(sum(element))

    return out


def exercise_3_9_test():
    assert exercise_3_9([[1, 2, 3], (5, 6), [4, 1], []]) == [6, 11, 5, 0]
    assert exercise_3_9([[],[4],(1,2),[3,4],(5,6,7)]) == [0,4,3,7,18]
    print("tests passed")


if __name__ == "__main__":
    exercise_3_9_test()
