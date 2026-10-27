import unittest


def factorial(n: int):
    if n < 0:
        raise ValueError("factorial can't be negative")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i

    return factorial


class TestFactorial(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-4)

if __name__ == "__main__":
    print("---4.3---")
    unittest.main()
