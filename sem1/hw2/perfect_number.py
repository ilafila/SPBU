from unittest import TestCase, main


def perfect_number(a):
    if type(a) != int or a < 1:
        raise ValueError
    amount_deliteli = 0
    for i in range(1, a):
        if i != 0 and a % i == 0:
            amount_deliteli += i
    if a == amount_deliteli:
        return True
    return False


class Validator(TestCase):
    def test1(self):
        self.assertFalse(perfect_number(1), False)

    def test2(self):
        self.assertTrue(perfect_number(6))

    def test3(self):
        self.assertTrue(perfect_number(28))

    def test4(self):
        self.assertRaises(ValueError, perfect_number, [6])

    def test5(self):
        self.assertRaises(ValueError, perfect_number, -28)


main()
