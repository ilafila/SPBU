from memory_profiler import profile, time
from unittest import TestCase, main
import sys


@profile
def factorial(a):
    fac = 1
    if a == 0:
        return 1
    if type(a) != int or a < 0:
        raise ValueError
    for i in range(1, a + 1):
        fac *= i
    return fac


@profile
def start_rec(b):
    sys.setrecursionlimit(100000)
    return factorial_rec(b)


def factorial_rec(b):
    if b == 0:
        return 1
    if (type(b) != int) or b < 0:
        raise ValueError
    return 1 if b == 1 else b * factorial_rec(b - 1)


class Tests(TestCase):
    def test1(self):
        self.assertRaises(ValueError, factorial, '7')

    def test2(self):
        self.assertRaises(ValueError, factorial, "ab")

    def test3(self):
        self.assertRaises(ValueError, factorial, 9.0)

    def test4(self):
        self.assertEqual(factorial(10), 3628800)

    def test5(self):
        self.assertEqual(factorial(0), 1)

    def test6(self):
        self.assertRaises(ValueError, factorial, -2)

    def test7(self):
        self.assertRaises(ValueError, factorial, 10.5)

    def test8(self):
        self.assertRaises(ValueError, factorial, [7])

    def test9(self):
        self.assertRaises(ValueError, start_rec, "7")

    def test10(self):
        self.assertRaises(ValueError, start_rec, "ab")

    def test11(self):
        self.assertRaises(ValueError, start_rec, 9.0)

    def test12(self):
        self.assertEqual(start_rec(10), 3628800)

    def test13(self):
        self.assertEqual(start_rec(0), 1)

    def test14(self):
        self.assertRaises(ValueError, start_rec, -2)

    def test15(self):
        self.assertRaises(ValueError, start_rec, 10.5)

    def test16(self):
        self.assertRaises(ValueError, start_rec, [7])


wtime = time.process_time()
factorial(3)
print(time.process_time() - wtime)
start_rec(3)
print(time.process_time() - wtime)
main()
