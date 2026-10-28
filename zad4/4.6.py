import unittest


def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item

    return sum


class TestSumSeq(unittest.TestCase):
    def test_no_nasted_list(self):
        self.assertEqual(sum_seq([1, 2, 3]), 6)

    def test_no_nasted_tuple(self):
        self.assertEqual(sum_seq((1, 2, 3)), 6)

    def test_nasted_list(self):
        self.assertEqual(sum_seq([1, [1, 2, 3], 3]), 10)

    def test_nasted_tuple(self):
        self.assertEqual(sum_seq([1, (1, 2, 3), 3]), 10)

    def test_double_nasted_list(self):
        self.assertEqual(sum_seq([1, [1, [2, 3, 4], 3], 3]), 17)

    def test_double_nasted_tuple(self):
        self.assertEqual(sum_seq([1, (1, (2, 3, 4), 3), 3]), 17)

    def test_double_nasted_mixed(self):
        self.assertEqual(sum_seq([1, (1, [2, 3, 4], 3), 3]), 17)

    def test_multiple_lists_and_tuples(self):
        self.assertEqual(
            sum_seq([1, (1, [2, 3, 4], 3), 3, (1, 2), (2, (3, 2)), [[[4]]]]), 31
        )


if __name__ == "__main__":
    print("---4.6---")
    unittest.main()
