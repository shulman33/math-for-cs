import unittest
from totient import prime_fac as prime_fac
from totient import phi as phi
# written by Zirm
class test_totient(unittest.TestCase):
    def test_prime_fac(self):
        self.assertEqual(prime_fac(216), [(2,3), (3,3)])
        self.assertEqual(prime_fac(2150), [(2,1), (5,2), (43,1)])
        self.assertEqual(prime_fac(12345678), [(2,1), (3,2), (47,1), (14593,1)])
        print('prime fac works!')
    def test_phi(self):
        self.assertEqual(phi(prime_fac(216)),72)
        self.assertEqual(phi(prime_fac(210)),48)
        self.assertEqual(phi(prime_fac(165)),80)
        self.assertEqual(phi(prime_fac(12345678)),4027392)
        self.assertEqual(phi([(127,1), (9721,1)]),1224720)
        print('phi works!')
if __name__ == '__main__':
    unittest.main()
    
