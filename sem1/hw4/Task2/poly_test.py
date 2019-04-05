from poly_logic import diff
from unittest import TestCase, main


class Validator(TestCase):
    def test1(self):
        self.assertRaises(TypeError, diff, 14567)

    def test2(self):
        self.assertEqual(diff('- 3x^2 + 2x + 1'), '- 6x + 2')

    def test3(self):
        self.assertEqual(diff('3x^7 + 10x^5 - 4x^2 + 3'), '21x^6 + 50x^4 - 8x')

    def test4(self):
        self.assertEqual(diff('10x^3 - 20x'), '30x^2 - 20')

    def test5(self):
        self.assertEqual(diff('2x^2 + 5'), '4x')


main()
