import unittest

def gcd(a,b):
    if b > 0:
        return gcd(b, a % b)
    return a

def add_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    gcd1 = gcd(licznik, mianownik)
    return [licznik // gcd1, mianownik // gcd1]

def sub_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    gcd1 =  gcd(licznik, mianownik)
    return [licznik //gcd1, mianownik //gcd1]

def mul_frac(frac1, frac2):
    licznik = frac1[0] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    gcd1 =  gcd(licznik, mianownik)
    return [licznik //gcd1, mianownik //gcd1]

def div_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1]
    mianownik = frac1[1] * frac2[0]
    if mianownik == 0:
        raise ValueError("Dzielenie przez zero!")
    gcd1 =  gcd(licznik, mianownik)
    return [licznik //gcd1, mianownik //gcd1]

def is_positive(frac):
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    frac1_value = frac1[0] * frac2[1]
    frac2_value = frac2[0] * frac1[1]
    if frac1_value < frac2_value:
        return -1
    elif frac1_value > frac2_value:
        return 1
    return 0

def frac2float(frac):
    return frac[0] / frac[1]

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [1, 2]
        self.f2 = [1, 3]
        self.f3 = [-1, 2]
        self.f4 = [1, -2]
        self.f5 = [3, 6]
        
    def test_add_frac(self):
        self.assertEqual(add_frac(self.f1, self.f2), [5, 6])
        self.assertEqual(add_frac(self.f1, self.f3), [0, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f1, self.f2), [1, 6])
        self.assertEqual(sub_frac(self.f2, self.f1), [-1, 6])  

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f1, self.f2), [1, 6])
        self.assertEqual(mul_frac(self.f1, self.f3), [-1, 4])  

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f1, self.f2), [3, 2])
        self.assertEqual(div_frac(self.f2, self.f5), [2, 3])

    def test_is_positive(self):
        self.assertTrue(is_positive(self.f1))
        self.assertFalse(is_positive(self.f3))
        self.assertFalse(is_positive(self.f4))
        self.assertTrue(is_positive([10, 5154]))  

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.f1))
        self.assertFalse(is_zero(self.f5))  

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f1, self.f2), 1)
        self.assertEqual(cmp_frac(self.f1, self.f1), 0)
        self.assertEqual(cmp_frac(self.f2, self.f1), -1)
        self.assertEqual(cmp_frac(self.f1, self.f5), 0)  

    def test_frac2float(self):
        self.assertEqual(frac2float(self.f1), 0.5)
        self.assertEqual(frac2float(self.f3), -0.5)
        self.assertEqual(frac2float([-5, 8]), -0.625)  
        
    def tearDown(self):
        self.zero = []
        self.f1 = []
        self.f2 = []
        self.f3 = []
        self.f4 = []
        self.f5 = []
        
if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
