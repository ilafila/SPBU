from smile_logic import check
from unittest import TestCase, main


class Validator(TestCase):
    def test1(self):
        self.assertTrue(check('Киркоров(антихайп)'))

    def test2(self):
        self.assertTrue(check('внешний долг США over 9000'))

    def test3(self):
        self.assertTrue(check('()[]{}'))

    def test4(self):
        self.assertTrue(check('[(){{}()}]()'))

    def test5(self):
        self.assertFalse(check('пРифФкИи [) >3'))

    def test6(self):
        self.assertFalse(check('({[)]'))

    def test7(self):
        self.assertFalse(check('{а{ _ __ @{'))

    def test8(self):
        self.assertRaises(ValueError, check, (1, 2, -1))

    def test9(self):
        self.assertRaises(ValueError, check, 123)


main()
