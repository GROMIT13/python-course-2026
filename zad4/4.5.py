import unittest


def odwracanie_recursive(L: list, left: int, right: int): 
    if left < 0:
        left = len(L)+left

    if right < 0:
        right= len(L)+right

    if left > right:
        return

    L[left], L[right] = L[right], L[left]
    odwracanie_recursive(L, left+1, right-1)


def odwracanie_iterative(L: list, left: int, right: int):
    if left < 0:
        left = len(L)+left

    if right < 0:
        right= len(L)+right
        
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

class OdwracanieRekurencyjneTest(unittest.TestCase):
    def test_reverse_all(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,0,len(L)-1)
        self.assertEqual(L,[10,9,8,7,6,5,4,3,2,1])

    def test_reverse_left(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,2,len(L)-1)
        self.assertEqual(L,[1,2,10,9,8,7,6,5,4,3])

    def test_reverse_right(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,0,len(L)-3)
        self.assertEqual(L,[8,7,6,5,4,3,2,1,9,10])

    def test_reverse_both_sides(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,2,len(L)-3)
        self.assertEqual(L, [1,2,8,7,6,5,4,3,9,10])

    def test_left_gt_right(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,8,len(L)-6)
        self.assertEqual(L, [ 1,2,3,4,5,6,7,8,9,10 ])

    def test_left_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,-6,len(L)-2)
        self.assertEqual(L, [1,2,3,4,9,8,7,6,5,10 ])
        
    def test_right_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,3,-2)
        self.assertEqual(L, [1,2,3,9,8,7,6,5,4,10 ])

    def test_both_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_recursive(L,-7,-3)
        self.assertEqual(L, [1,2,3,8,7,6,5,4,9,10 ])
        

class OdwracanieIteracyjneTest(unittest.TestCase):
    def test_reverse_all(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,0,len(L)-1)
        self.assertEqual(L,[10,9,8,7,6,5,4,3,2,1])

    def test_reverse_left(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,2,len(L)-1)
        self.assertEqual(L,[1,2,10,9,8,7,6,5,4,3])

    def test_reverse_right(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,0,len(L)-3)
        self.assertEqual(L,[8,7,6,5,4,3,2,1,9,10])

    def test_reverse_both_sides(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,2,len(L)-3)
        self.assertEqual(L, [1,2,8,7,6,5,4,3,9,10])

    def test_left_gt_right(self):
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,8,len(L)-6)
        self.assertEqual(L, [ 1,2,3,4,5,6,7,8,9,10 ])

    def test_left_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,-6,len(L)-2)
        self.assertEqual(L, [1,2,3,4,9,8,7,6,5,10 ])
        
    def test_right_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,3,-2)
        self.assertEqual(L, [1,2,3,9,8,7,6,5,4,10 ])

    def test_both_as_negative(self): 
        L = [ 1,2,3,4,5,6,7,8,9,10 ]
        odwracanie_iterative(L,-7,-3)
        self.assertEqual(L, [1,2,3,8,7,6,5,4,9,10 ])

if __name__ == "__main__":
    print("---4.5---")
    unittest.main()
