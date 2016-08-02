import unittest
import math

class Fibonacci(object):

    def recursive_fibonacci(self, n):
        """Linear time fibonacci algorithm. 
        
        Args:
            :n positive int: n should be an int >= 0
        Return:
            the value of the nth fibonacci number

        int() type conversion happens. Error isn't handled by class.
        """
        n = int(n)
        self._value_check(n)
        if self._basecase(n):
            return n
        return self.recursive_fibonacci(n-1) + self.recursive_fibonacci(n-2)

    def constant_fibonacci(self, n):
        """Constant time fibonacci algorithm. 
        
        Args:
            :n positive int: n should be an int >= 0
        Return:
            the value of the nth fibonacci number

        int() type conversion happens. Error isn't handled by class.
        """
        n = int(n)
        self._value_check(n)
        if self._basecase(n):
            return n
        Phi = ((1 + math.sqrt(5))/2)**n
        nphi = (1 - math.sqrt(5))/2**n
        return int(round(((Phi - nphi)/math.sqrt(5))))

    def _basecase(self, n):
        if n == 0 or n == 1:
            return True
        return False

    def _value_check(self, n):
        if n < 0:
            raise ValueError('Please provide positive integers')

class testingFibonacci(unittest.TestCase):

    def test_recursive_fibonacci(self):
        n = Fibonacci().recursive_fibonacci(0)
        self.assertEquals(n, 0)
        n = Fibonacci().recursive_fibonacci(2)
        self.assertFalse(n==2)
        self.assertTrue(n, 1)
        n = Fibonacci().recursive_fibonacci(1)
        self.assertEquals(n, 1)
        n = Fibonacci().recursive_fibonacci(10)
        self.assertEquals(n, 55)
        self.assertRaises(ValueError, Fibonacci().recursive_fibonacci, -1)

    def test_constant_fibonacci(self):
        n = Fibonacci().constant_fibonacci(0)
        self.assertEquals(n, 0)
        n = Fibonacci().constant_fibonacci(2)
        self.assertFalse(n==2)
        self.assertTrue(n, 1)
        n = Fibonacci().constant_fibonacci(1)
        self.assertEquals(n, 1)
        n = Fibonacci().constant_fibonacci(10)
        self.assertEquals(n, 55)
        self.assertRaises(ValueError, Fibonacci().constant_fibonacci, -1)


if __name__ == '__main__':
    unittest.main()
    
