from balls_collide import balls_shoot
from unittest import TestCase, main


class Validator(TestCase):
    def test1(self):
        self.assertRaises(ValueError, balls_shoot, (1, 2, -1), (1, 3, -2))

    def test2(self):
        self.assertTrue(balls_shoot((1.2, 2.5, 3.6), (1.2, 2.5, 3.6)))

    def test3(self):
        self.assertTrue(balls_shoot((-1, 1, 2), (3, 4, 3)))

    def test4(self):
        self.assertTrue(balls_shoot((-1, 1, 5), (3, 4, 7)))

    def test5(self):
        self.assertFalse(balls_shoot((-1, 1, 1), (3, 4, 1)))


main()
