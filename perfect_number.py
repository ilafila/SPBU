from unittest import TestCase, main
def perfect_number(a):
    if type(a) != int or a< 1:
        return "ValueError"
    amount_deliteli = 0
    if a == 0:
        return False
    for i in range(0, abs(a)):
        if (i != 0)  and (a % i == 0):
            amount_deliteli +=i
    if a == amount_deliteli:
        return True
    else:
      return False



print(perfect_number(6))


class Validator(TestCase):
    def test_correct_values(self):
        if not self.assertFalse(perfect_number(1), False):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertTrue(perfect_number(6)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertTrue(perfect_number(28)):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(perfect_number([6]), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")
        if not self.assertEqual(perfect_number(-28), "ValueError"):
            print("Test passed")
        else:
            print("Test failed")

main()