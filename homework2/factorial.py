from memory_profiler import profile, time
from unittest import TestCase, main
import sys
@profile
def factorial(a):
    fac=1
    if (a==0):
        return 1
    if (type(a) != int) or a<0:
        return "ValueError"
    for i in range(a):
        fac *=(i+1)
    return fac




#chislo1=int(input())
#print(factorial(b))

@profile
def startRec(b):
    sys.setrecursionlimit(100000)
    return factorial_rec(b)

def factorial_rec(b):
    if (b==0):
        return 1
    if (type(b) != int) or b<0:
        return "ValueError"
    return 1 if b == 1 else b * factorial_rec(b - 1)


#chislo=int(input())
wtime = time.process_time()
factorial(10)
print(time.process_time() - wtime )






class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertEqual(factorial("7"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial("ab"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial(9.0), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial(-2), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial(10.5), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(factorial([7]), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec("7"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec("ab"), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec(9.0), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec(10), 3628800):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec(0), 1):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec(-2), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec(10.5), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(startRec([7]), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")


main()

