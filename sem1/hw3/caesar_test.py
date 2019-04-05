from caesar_logic import encrypt, decrypt
from unittest import TestCase, main


class Validator(TestCase):
    def test1(self):
        self.assertRaises(TypeError, encrypt, 2.5, 'ABD')

    def test2(self):
        self.assertEqual(encrypt(3, 'ABD'), 'DEG')

    def test3(self):
        self.assertEqual(encrypt(4, 'azx'), 'edb')

    def test4(self):
        self.assertTrue(decrypt(3, 'dca'), 'azx')

    def test5(self):
        self.assertEqual(decrypt(3, 'DEG'), 'ABD')

    def test6(self):
        self.assertRaises(TypeError, decrypt, 'abc', 'cdE')


main()
