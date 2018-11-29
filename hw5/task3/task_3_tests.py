from task_3 import Roman
from unittest import TestCase, main


class Validator(TestCase):
    def test_raises(self):
        with self.assertRaises(ValueError):
            Roman(2018)

        with self.assertRaises(ValueError):
            Roman(300) * Roman(10)

        with self.assertRaises(ValueError):
            Roman(2500) - Roman(10)

        with self.assertRaises(ValueError):
            Roman(0)

        with self.assertRaises(ValueError):
            Roman(1) - Roman(1)

        with self.assertRaises(ValueError):
            Roman(-1)

    def test1(self):
        self.assertEqual(Roman(34) + Roman(1965), Roman(1999))

    def test2(self):
        self.assertEqual(str(Roman(8)), 'VIII')

    def test3(self):
        self.assertEqual(str(Roman(10)), 'X')

    def test4(self):
        self.assertEqual(str(Roman(1999)), 'MCMXCIX')

    def test5(self):
        self.assertEqual(int(Roman(10)), 10)

    def test6(self):
        self.assertEqual(int(Roman(10)), 10)

    def test7(self):
        self.assertEqual(int(Roman(1110)), 1110)

    def test8(self):
        self.assertEqual(int(Roman(10)), 10)

    def test9(self):
        self.assertTrue(Roman(10) + Roman(10) == Roman(20))

    def test10(self):
        self.assertTrue(Roman(1890) - Roman(10) == Roman(1880))

    def test11(self):
        self.assertTrue(Roman(1699) // Roman(10) == Roman(169))

    def test12(self):
        self.assertTrue(Roman(1699) % Roman(10) == Roman(9))

    def test13(self):
        self.assertTrue(Roman(10) + Roman(10) == Roman(20))

    def test14(self):
        self.assertFalse(Roman(10) == Roman(20))

    def test15(self):
        self.assertEqual(Roman(1000) - Roman(10), Roman(990))

    def test16(self):
        self.assertEqual(Roman(100) - Roman(10) - Roman(10), Roman(80))

    def test17(self):
        self.assertEqual(Roman(100) * Roman(10), Roman(1000))

    def test18(self):
        self.assertEqual(Roman(100) * Roman(10), Roman(1000))

    def test19(self):
        self.assertEqual(Roman(5) * Roman(5) * Roman(5), Roman(125))

    def test20(self):
        self.assertEqual(Roman(100) * Roman(10), Roman(1000))

    def test21(self):
        self.assertEqual(Roman(1290) // Roman(100), Roman(12))

    def test22(self):
        self.assertEqual(Roman(1290) // Roman(100) // Roman(10), Roman(1))

    def test23(self):
        self.assertEqual(Roman(1290) % Roman(100), Roman(90))

    def test24(self):
        self.assertEqual(Roman(1294) % Roman(100) % Roman(10), Roman(4))

    def test25(self):
        self.assertEqual((Roman(2) + Roman(100) - Roman(2))
                         // Roman(100), Roman(1))

    def test26(self):
        self.assertEqual(Roman(1) * Roman(2) * Roman(9) // Roman(3) -
                         Roman(9) % Roman(5) - Roman(9) // Roman(5), Roman(1))

    def test27(self):
        self.assertEqual(str(Roman(int(Roman(10)) * int(Roman(100)))
                             - Roman(int(Roman(111)) * int(Roman(9)))), 'I')

    def test28(self):
        self.assertEqual(str(Roman(int(Roman(1000)) + int(Roman(900))) +
                             Roman(int(Roman(90)) + int(Roman(9)))), 'MCMXCIX')


main()
