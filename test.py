__author__ = 'x1m'

import unittest
import funcs

list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]
list_n_primes = [4, 6, 8, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 26, 120, 440, 550, 680]

list_pals = ['123321', '123321', '9009', '55566555']
list_n_pals = ['4684', '88465412', '4846']

class IsPrime(unittest.TestCase):
    def test_prime_primes(self):
        for i in list_primes:
            assert funcs.prime(i) == True
    def test_prime_n_primes(self):
        for i in list_n_primes:
            assert funcs.prime(i) == False

class IsPal(unittest.TestCase):
    def test_for_pal(self):
        for i in  list_pals:
            assert funcs.isPal(i)

    def test_for_n_pal(self):
        for i in list_n_pals:
            assert not funcs.isPal(i)




if '__name__' == '__main__':
    unittest.main()