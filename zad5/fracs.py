#!usr/bin/env python

from math import gcd 

def add_frac(frac1, frac2):
    frac1, frac2 = find_common_denominator(frac1, frac2)
    return [frac1[0] + frac2[0], frac1[1]]

def sub_frac(frac1, frac2): 
    frac1, frac2 = find_common_denominator(frac1, frac2)
    return [frac1[0] - frac2[0], frac1[1]]

def mul_frac(frac1, frac2): 
    frac1, frac2 = find_common_denominator(frac1, frac2)
    frac = [frac1[0] * frac2[0],frac1[1] * frac2[1]]
    return fix_format(frac)

def div_frac(frac1, frac2):
    frac1, frac2 = find_common_denominator(frac1, frac2)
    frac2[0], frac2[1] = frac2[1], frac2[0]
    frac2 = fix_format(frac2)
    frac = [frac1[0] * frac2[0],frac1[1] * frac2[1]]
    return fix_format(frac)

def is_positive(frac):
    frac = fix_format(frac)
    return True if frac[0] >= 0 else False

def is_zero(frac):
    frac = fix_format(frac)
    return True if frac[0] == 0 else False

def cmp_frac(frac1,frac2):
    frac1, frac2 = find_common_denominator(frac1,frac2)
    if frac1[0] > frac2[0]:
        return 1
    elif frac1[0] == frac2[0]:
        return 0
    else:
        return -1

def frac2float(frac):
    frac = fix_format(frac)
    return frac[0]/frac[1]

def fix_format(frac):
    """
    Helper function
    Returns ZeroDivisionError if fraction is invalid.
    Fixes sign to alvays be in iterator.
    If fraction is valid returns fraction with smalest denominator
    """
    if frac[1] == 0:
        raise ZeroDivisionError
    
    div = gcd(int(frac[0]),int(frac[1]))

    if frac[1] < 0:
        return [int(-frac[0]/div),int(-frac[1]/div)]
    
    return [int(frac[0]/div),int(frac[1]/div)]

def find_common_denominator(frac1, frac2):

    """
    Helper function
    Returns ZeroDivisionError if fraction is invalid.
    Returns both fractions with common denominator.
    """
    frac1 = fix_format(frac1)
    frac2 = fix_format(frac2)
    lcm = frac1[1] * frac2[1] / gcd(frac1[1],frac2[1])
    frac1_mul = lcm / frac1[1]
    frac2_mul = lcm / frac2[1]
    frac1 = [frac1[0] * frac1_mul, lcm]
    frac2 = [frac2[0] * frac2_mul, lcm]
    return frac1,frac2


import unittest


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [ 0,1 ]

    def test_add_frac(self):
        # set correct numerator addiotion
        self.assertEqual(add_frac([1,2],[2,2]),[3,2])
        # add zero
        self.assertEqual(add_frac([0,3],[1,2]),[1,2]) 
        # set correct denominator and numerator (increased)
        self.assertEqual(add_frac([2,3],[1,2]),[7,6])
        # set correct denominator and numerator (decreased)
        self.assertEqual(add_frac([5,5],[5,15]),[4,3])
        # test negative values
        self.assertEqual(add_frac([-1,-2],[1,4]),[3,4])
        self.assertEqual(add_frac([-1,2],[1,4]),[-1,4])

    def test_sub_frac(self):
        # set correct numerator subtraction
        self.assertEqual(sub_frac([2,2],[1,2]),[1,2])
        # sub zero
        self.assertEqual(sub_frac([1,2],[0,3]),[1,2]) 
        # zero sub
        self.assertEqual(sub_frac([0,3],[1,2]),[-1,2]) 
        # set correct denominator and numerator (increased)
        self.assertEqual(sub_frac([2,3],[1,2]),[1,6])
        # set correct denominator and numerator (decreased)
        self.assertEqual(sub_frac([5,5],[5,15]),[2,3])
        # test negative values
        self.assertEqual(sub_frac([-1,-2],[1,4]),[1,4])
        self.assertEqual(sub_frac([-1,2],[1,4]),[-3,4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1,2],[1,2]),[1,4]) 
        self.assertEqual(mul_frac([2,2],[1,2]),[1,2]) 
        self.assertEqual(mul_frac([1,-2],[-1,2]),[1,4]) 
        self.assertEqual(mul_frac([1,-2],[-1,-2]),[-1,4]) 
        self.assertEqual(mul_frac([0,3],[-1,2]),[0,1])
        self.assertEqual(mul_frac([2,3],[7,11]),[14,33])

    def test_div_frac(self): 
        self.assertEqual(div_frac([1,2],[1,2]),[1,1]) 
        self.assertEqual(div_frac([2,2],[1,2]),[2,1]) 
        self.assertEqual(div_frac([1,-2],[-1,2]),[1,1]) 
        self.assertEqual(div_frac([1,-2],[-1,-2]),[-1,1]) 
        self.assertEqual(div_frac([2,3],[7,11]),[22,21])
        self.assertEqual(div_frac([0,3],[-1,2]),[0,1])
        self.assertRaises(ZeroDivisionError, lambda : div_frac([1,2],[0,1]))

    def test_is_positive(self):
        self.assertEqual(is_positive([1,2]),True)
        self.assertEqual(is_positive([0,2]),True)
        self.assertEqual(is_positive([-1,2]),False)
        self.assertEqual(is_positive([0,-2]),True)


    def test_is_zero(self):
        self.assertEqual(is_zero([0,2]), True)
        self.assertEqual(is_zero([0,-2]), True)
        self.assertEqual(is_zero([0,12]), True)
        self.assertEqual(is_zero([6,2]), False)
        self.assertEqual(is_zero([6,17]), False)
 
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,2],[2,3]), -1)
        self.assertEqual(cmp_frac([2,3],[1,2]), 1)
        self.assertEqual(cmp_frac([1,2],[1,2]), 0)
        self.assertEqual(cmp_frac([2,4],[2,4]), 0) 

    def test_frac2float(self):
        self.assertEqual(frac2float([1,2]),0.5)
        self.assertEqual(frac2float([0,3]),0)
        self.assertRaises(ZeroDivisionError, lambda : frac2float([1,0]))
        
    def test_fix_fromat(self):
        self.assertEqual(fix_format([-1,-2]),[1,2])
        self.assertEqual(fix_format([1,-2]),[-1,2])
        self.assertEqual(fix_format([0,-2]),[0,1])
        self.assertEqual(fix_format([0,2]),[0,1])
        self.assertEqual(fix_format([4,2]),[2,1])
        self.assertEqual(fix_format([4,-2]),[-2,1])
        self.assertEqual(fix_format([-4,-2]),[2,1])
        self.assertRaises(ZeroDivisionError,lambda : fix_format([0,0]))
        self.assertRaises(ZeroDivisionError,lambda : fix_format([1,0]))

    def test_find_common_denominator(self):
        self.assertEqual(find_common_denominator([2,21],[1,6]),([4,42],[7,42])) 
        self.assertRaises(ZeroDivisionError, lambda : find_common_denominator([2,21],[1,0]))
        self.assertRaises(ZeroDivisionError, lambda : find_common_denominator([2,0],[1,6]))
        

    def tearDown(self):
        pass


if __name__ == "__main__": 
    unittest.main()
