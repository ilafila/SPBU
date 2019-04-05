import math
from unittest import TestCase, main


def pascal_tree(number_of_lines):
    if type(number_of_lines) != int or number_of_lines < 0:
        raise ValueError
    new_list = [[1]]
    for n in range(1, number_of_lines+1):
        origin_list = []
        for k in range(0, n + 1):
            origin_list.append(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
        new_list.append(origin_list)
    return new_list


class Validator(TestCase):
    def test1(self):
        self.assertRaises(ValueError, pascal_tree, 'abc')

    def test2(self):
        self.assertEqual(pascal_tree(0), [[1]])

    def test3(self):
        self.assertEqual(pascal_tree(2), [[1], [1, 1], [1, 2, 1]])

    def tesst4(self):
        self.assertRaises(ValueError, pascal_tree, -3)

    def test5(self):
        self.assertEqual(pascal_tree(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


main()
