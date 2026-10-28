import unittest


def flatten(sequence):
    flat_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list


class TestFlatten(unittest.TestCase):
    def test_no_need_to_flatten(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_list(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_flatten_tuple(self):
        self.assertEqual(flatten([1, (2, 3), 4]), [1, 2, 3, 4])

    def test_flatten_nasted_list(self):
        self.assertEqual(
            flatten([1, [[1, 2, 3, [4]], 5], 7, 5]), [1, 1, 2, 3, 4, 5, 7, 5]
        )

    def test_flatten_nasted_tuple(self):
        self.assertEqual(
            flatten([1, ((1, 2, 3, (4, 3)), 5), 7, 5]), [1, 1, 2, 3, 4, 3, 5, 7, 5]
        )

    def test_tuple_and_list(self):
        self.assertEqual(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]),[1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
    print("---4.7---")
    unittest.main()
