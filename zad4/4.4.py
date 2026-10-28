import unittest


def fibonacci(n :int):
    if n < 0:
        raise ValueError("negative fibonacci values does not exist")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    c = 0
    for _ in range (n-1):
       c = a + b
       a = b
       b = c

    return c

class TestFibonacci(unittest.TestCase):
    def test_positive(self): 
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)
        self.assertEqual(fibonacci(4),3)
        self.assertEqual(fibonacci(5),5)
        self.assertEqual(fibonacci(6),8)
        self.assertEqual(fibonacci(7),13)
        self.assertEqual(fibonacci(8),21)
        self.assertEqual(fibonacci(9),34)
        self.assertEqual(fibonacci(10),55)
        self.assertEqual(fibonacci(11),89)
        self.assertEqual(fibonacci(12),144)
        self.assertEqual(fibonacci(20),6765)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

        with self.assertRaises(ValueError):
            fibonacci(-7)

    
if __name__ == "__main__":
    print("---4.4---")
    unittest.main()
    
